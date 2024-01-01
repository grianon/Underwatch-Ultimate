> This is a fork to support 3440x1440 21:9. If you need 1080p, use the og repo.

<br>

An application to controls sex toys based on Overwatch 2 gameplay. Here's a [list](https://iostindex.com/?filter0ButtplugSupport=4) of supported devices.

# Instructions:

- Install and run [Intiface Central](https://intiface.com/central/).
- Download and run [a release of Underwatch Ultimate](https://github.com/Furimanejo/Underwatch-Ultimate/releases).
- One the tab "Device Control" click connect to intiface. Make sure your toys are on and appear on the list of connected devices.
- Play Overwatch, you can test the app on the training range.

# Observations:

- If you want to use the overlay, make sure your game is running in borderless display mode.
- The gameplay detection should work even with custom color schemes, let me know if it doesn't.

# Support:

Join my [discord server](https://discord.gg/wz2qvkuEyJ) if you have any questions, suggestions or just wanna talk about it.

And if you liked the app and want to support me, you can donate at https://donate.stripe.com/7sI3eZcExdGrc5WeUU

<br><br><br>

# Contributing

### How to run locally

- Install python `3.9.13` with pip
- Install dependencies `$ pip install -r requirements.txt`
- Run `$ python underwatch.py`

### How to build

- Run `$ ./build.bat`

### How to add new triggers:

- Run `$ python get_screen_coords.py` (esc to quit)
- Select the item on the screen to match against (ie. elimination logo)
- Record the captured coordinates in the console as well as the exported screenshot now located in `/tmp_rect_captures`.
- Rename the screenshot to something unique (ie. elimation.png) and move to `/templates`
- Add the recorded coordinates to the `regions` section in `config.py` using others as an example
- Add the new region to the `detectables` section in `config.py` making sure to reference the correct filename you added to `/templates`
  - note: the `threshold` is the "sensitivity" of recognition. If you find that its triggering too much/too little, then you can increase or decrease this number. Running underwatch-ultimate locally will log the configured threshold vs the actual threshold if triggered to make this configuration easy to test.
- Lastly, Add the new detectable to the `regionKeysByDetectableTypes` in `config.py`. The detectable types are groups of defined regions on the screen. You can show overlay in the running program to view these and configure by example given the other items.
