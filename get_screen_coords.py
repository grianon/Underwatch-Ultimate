import tkinter as tk
from PIL import Image, ImageGrab, ImageTk
import os
import shutil


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.attributes("-fullscreen", True)
        self.attributes("-alpha", 0.3)
        self.attributes("-topmost", True)
        self.overrideredirect(True)

        self.canvas = tk.Canvas(self, cursor="cross", bg="white")
        self.canvas.pack(fill="both", expand=True)

        # Bindings
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release_finder_mode)
        self.canvas.bind("<Motion>", self.on_motion)

        # Initialize variables
        self.rect = None
        self.start_x = None
        self.start_y = None
        self.count = 0

        # Cursor lines
        self.cursor_line_vertical = self.canvas.create_line(
            0, 0, 0, 0, fill="red", width=1
        )
        self.cursor_line_horizontal = self.canvas.create_line(
            0, 0, 0, 0, fill="red", width=1
        )

        # Preview box
        self.preview_window = tk.Toplevel(self)
        self.preview_window.overrideredirect(True)
        self.preview_window.attributes("-topmost", True)
        self.preview_label = tk.Label(
            self.preview_window, borderwidth=1, relief="solid"
        )
        self.preview_label.pack()

        # Bind escape key to close application
        self.bind("<Escape>", self.close)

        # Directory for screenshots
        self.screenshot_dir = "tmp_rect_captures"
        if os.path.exists(self.screenshot_dir):
            shutil.rmtree(self.screenshot_dir)

    def close(self, event=None):
        self.preview_window.destroy()
        self.destroy()

    def on_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(
            self.start_x, self.start_y, self.start_x, self.start_y, outline="red"
        )
        self.update_cursor_lines(event.x, event.y)

    def on_drag(self, event):
        self.canvas.coords(self.rect, self.start_x, self.start_y, event.x, event.y)
        self.update_cursor_lines(event.x, event.y)
        self.update_preview(event.x, event.y)

    def create_label_at_rect(self, rect, number):
        x1, y1, x2, y2 = self.canvas.coords(rect)
        label = self.canvas.create_text(
            x1 + 10, y1 + 10, text=str(number), fill="red", font=("Arial", 16)
        )
        return label

    def on_release_finder_mode(self, event):
        bbox = self.canvas.coords(self.rect)
        print(f"{self.count+1}: [{bbox[1]}, {bbox[3]}, {bbox[0]}, {bbox[2]}]")

        if self.rect:
            self.count += 1
            self.create_label_at_rect(self.rect, self.count)
            self.save_screenshot(bbox)

    def save_screenshot(self, bbox):
        # Ensure the directory for saving screenshots exists
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)

        # Calculate the absolute screen coordinates for the screenshot
        screen_x = self.winfo_rootx() + bbox[0]
        screen_y = self.winfo_rooty() + bbox[1]
        screen_bbox = (
            screen_x,
            screen_y,
            screen_x + (bbox[2] - bbox[0]),
            screen_y + (bbox[3] - bbox[1]),
        )

        # Capture and save the screenshot
        img = ImageGrab.grab(bbox=screen_bbox)
        img.save(os.path.join(self.screenshot_dir, f"{self.count}.png"))

    def on_motion(self, event):
        self.update_cursor_lines(event.x, event.y)
        self.update_preview(event.x, event.y)

    def update_cursor_lines(self, x, y):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        self.canvas.coords(self.cursor_line_vertical, x, 0, x, canvas_height)
        self.canvas.coords(self.cursor_line_horizontal, 0, y, canvas_width, y)

    def update_preview(self, x, y):
        preview_size = 120
        offset = 60
        screen_x = self.winfo_rootx() + x
        screen_y = self.winfo_rooty() + y
        bbox = (screen_x - 10, screen_y - 10, screen_x + 10, screen_y + 10)

        # Capture and display the preview
        img = ImageGrab.grab(bbox=bbox)
        img = img.resize((preview_size, preview_size), Image.NEAREST)
        tk_img = ImageTk.PhotoImage(img)

        self.preview_label.config(image=tk_img)
        self.preview_label.image = tk_img  # Keep reference

        # Position the preview window
        self.preview_window.geometry(
            f"{preview_size}x{preview_size}+{screen_x + offset}+{screen_y + offset}"
        )


if __name__ == "__main__":
    app = Application()
    app.mainloop()
