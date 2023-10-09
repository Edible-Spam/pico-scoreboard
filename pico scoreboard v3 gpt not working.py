from picounicorn import PicoUnicorn
picounicorn = PicoUnicorn()
import time

w = picounicorn.get_width()  # 16
h = picounicorn.get_height()  # 7

# From CPython Lib/colorsys.py
def hsv_to_rgb(h, s, v):
    if s == 0.0:
        return v, v, v
    i = int(h * 6.0)
    f = (h * 6.0) - i
    p = v * (1.0 - s)
    q = v * (1.0 - s * f)
    t = v * (1.0 - s * (1.0 - f))
    i = i % 6
    if i == 0:
        return v, t, p
    if i == 1:
        return q, v, p
    if i == 2:
        return p, v, t
    if i == 3:
        return p, q, v
    if i == 4:
        return t, p, v
    if i == 5:
        return v, p, q

playerXYcolours = (0, 114, 178)
playerABcolours = (255, 70, 160)

# Define team scores
scoreAB = 0
scoreXY = 0

# Define letters
BLANKSECTION = ["   " for i in range(h)]

NUMZERO = ["   ",
           "XXX",
           "X X",
           "X X",
           "X X",
           "XXX",
           "   "]

# ... Define other numbers ...

DASH = ["    ",
        "    ",
        "    ",
        " XX ",
        "    ",
        "    ",
        "    "]

scoredict = {
    0: NUMZERO,
    # Define other numbers here...
    "dash": DASH
}

# Function to clear display by setting pixels to black
def cleardisplay():
    for x in range(w):
        for y in range(h):
            picounicorn.set_pixel(x, y, 0, 0, 0)

# Function to update display with letters/numbers
def updatedisplay(scoreAB, scoreXY):
    scoreABpix = scoredict[scoreAB]
    scoreXYpix = scoredict[scoreXY]
    dashpix = scoredict["dash"]
    fulldisplay = [["{}{}{}{}{}".format(BLANKSECTION[i], scoreABpix[i], dashpix[i], scoreXYpix[i], BLANKSECTION[i])] for i in range(h)]
    return fulldisplay

# Main loop
while True:
    # Function to generate a 2D array to represent the current score in the format: PlayerABscore - PlayerXYscore
    currentdisplaymap = updatedisplay(scoreAB, scoreXY)

    # Display the initial scoreboard
    updatedisplay(scoreAB, scoreXY)

    # Check for button presses to update scores
    if picounicorn.is_pressed(picounicorn.BUTTON_A):
        scoreAB += 1
        if scoreAB > 9:
            scoreAB = 0
        time.sleep(0.2)  # Debounce the button press (adjust as needed)

    if picounicorn.is_pressed(picounicorn.BUTTON_B):
        scoreXY += 1
        if scoreXY > 9:
            scoreXY = 0
        time.sleep(0.2)  # Debounce the button press (adjust as needed)
