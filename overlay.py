from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import Qt
from win32gui import GetWindowText, GetForegroundWindow


class Overlay(QWidget):
    SCORE_LABEL_STYLE = "color: rgb(200, 0, 200); font: bold 18px;"
    DETECTION_DELAY_LABEL_STYLE = "color: rgb(200, 0, 200); font: bold 12px;"
    REGION_STYLE = "color: red; border: 1px solid red;"
    REGION_LABEL_STYLE = "color: red; font: bold 14px;"
    OVERWATCH_WINDOW_NAME = "Overwatch"

    def __init__(self, computer_vision) -> None:
        super().__init__(parent=None)
        self.computer_vision = computer_vision
        self.show_overlay_mode = 0
        self.show_regions_mode = 2
        self.init_ui()

    def init_ui(self):
        self.init_window()
        self.init_labels()
        self.init_regions()

    def init_window(self):
        self.setWindowTitle("overlay")
        self.resize(
            self.computer_vision.monitor["width"],
            self.computer_vision.monitor["height"],
        )
        self.setWindowFlags(self.window_flags())
        self.setAttribute(Qt.WA_TranslucentBackground)

    def window_flags(self):
        return (
            Qt.WindowTransparentForInput
            | Qt.WindowStaysOnTopHint
            | Qt.FramelessWindowHint
            | Qt.Tool
        )

    def init_labels(self):
        self.corners = self.create_label("", "border: 1px solid magenta;")
        self.points_label = self.create_label(
            "Score:", self.SCORE_LABEL_STYLE, [1000, 1020, 170, 420]
        )
        self.detection_delay_label = self.create_label(
            "Detection Delay:", self.DETECTION_DELAY_LABEL_STYLE, [1020, 1040, 170, 420]
        )

    def create_label(self, text, style, rect=None):
        label = QLabel(text, self)
        label.setStyleSheet(style)
        if rect:
            self.computer_vision.scale_to_monitor(rect)
            label.setGeometry(rect[2], rect[0], rect[3] - rect[2], rect[1] - rect[0])
        return label

    def init_regions(self):
        self.regions = {}
        for region_name, region_data in self.computer_vision.regions.items():
            rect, label = self.create_region_widgets(region_name, region_data)
            self.regions[region_name] = {"Rect": rect, "Label": label}

    def create_region_widgets(self, region_name, region_data):
        rect = self.create_label("", self.REGION_STYLE, region_data["Rect"])
        label = self.create_label(region_name, self.REGION_LABEL_STYLE)
        self.position_label(label, region_name, region_data["Rect"])
        return rect, label

    def position_label(self, label, region_name, rect_coords):
        if "Popup" in region_name:
            label.setGeometry(
                rect_coords[2] - 200,
                rect_coords[0],
                195,
                rect_coords[1] - rect_coords[0],
            )
            label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        else:
            label.setGeometry(rect_coords[2], rect_coords[0] - 100, 200, 100)
            label.setAlignment(Qt.AlignLeft | Qt.AlignBottom)

    def update(self):
        show = self.should_show_overlay()
        self.set_active(show)
        if show:
            self.update_regions()
            self.update_labels()

    def should_show_overlay(self):
        if self.show_overlay_mode == 0:
            return False
        elif self.show_overlay_mode == 1:
            return True
        elif self.show_regions_mode == 2:
            return GetWindowText(GetForegroundWindow()) == self.OVERWATCH_WINDOW_NAME
        return False

    def update_labels(self):
        self.points_label.setText(
            "Score: {0:.0f}".format(self.computer_vision.get_current_score())
        )
        self.detection_delay_label.setText(
            "Detection Delay: {0:4.0f} MS".format(
                1000 * self.computer_vision.detection_ping
            )
        )

    def set_active(self, value):
        if not value:
            self.corners.hide()
            self.points_label.hide()
            self.detection_delay_label.hide()
            for region in self.regions.values():
                region["Rect"].hide()
                region["Label"].setText("")
        else:
            self.corners.show()
            self.points_label.show()
            self.detection_delay_label.show()

    def update_regions(self):
        for region_name, region in self.regions.items():
            self.update_region(region_name, region)

    def update_region(self, region_name, region):
        if self.show_regions_mode == 0 or self.show_overlay_mode == 0:
            region["Rect"].hide()
            region["Label"].hide()
            region["Label"].setText("")
        elif self.show_regions_mode == 1:
            region["Rect"].show()
            region["Label"].show()
            region["Label"].setText(region_name)
        elif self.show_regions_mode == 2:
            self.update_region_matches(region, region_name)

    def update_region_matches(self, region, region_name):
        matches = self.computer_vision.regions[region_name].get("Matches", [])
        if not matches:
            region["Rect"].hide()
            region["Label"].hide()
            region["Label"].setText("")
        else:
            text = "\n".join(matches)
            region["Label"].setText(text)
            region["Label"].show()
            region["Rect"].show()

    def update_show_overlay_mode(self, new_mode_index):
        self.show_overlay_mode = new_mode_index
        self.update()

    def update_show_regions_mode(self, new_mode_index):
        self.show_regions_mode = new_mode_index
        self.update()
