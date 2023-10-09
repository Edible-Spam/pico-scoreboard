from picounicorn import PicoUnicorn
picounicorn = PicoUnicorn()
import time

w = picounicorn.get_width()#16
h = picounicorn.get_height()#7



playerXYcolours=(0,114,178)
playerABcolours=(255,70,160)

# Define team scores
team_a_score = 0
team_b_score = 0

# Define letters
BLANKSECTION= ["   " for i in range(h)] 

NUMZERO=["   ",
         "XXX",
         "X X",
         "X X",
         "X X",
         "XXX",
         "   "]
         
NUMONE=["   ",
        " X ",
        "XX ",
        " X ",
        " X ",
        "XXX",
        "   "]
        
NUMTWO=["   ",
        "XXX",
        "  X",
        "XXX",
        "X  ",
        "XXX",
        "   "]
        
NUMTHREE=["   ",
          "XXX",
          "  X",
          "XXX",
          "  X",
          "XXX",
          "   "]

NUMFOUR=["   ",
         "X X",
         "X X",
         "XXX",
         "  X",
         "  X",
         "   "]

NUMFIVE=["   ",
          "XXX",
          "X  ",
          "XXX",
          "  X",
          "XXX",
          "   "]
          
NUMSIX=["   ",
          "XXX",
          "X  ",
          "XXX",
          "X X",
          "XXX",
          "   "]          

NUMSEVEN=["   ",
          "XXX",
          "  X",
          "  X",
          " X ",
          " X ",
          "   "]
          
NUMEIGHT=["   ",
          "XXX",
          "X X",
          "XXX",
          "X X",
          "XXX",
          "   "]      

NUMNINE=["   ",
          "XXX",
          "X X",
          "XXX",
          "X X",
          "XXX",
          "   "]                  

DASH=["    ",
      "    ",
      "    ",
      " XX ",
      "    ",
      "    ",
      "    "]
      
scoredict={0:NUMZERO,1:NUMONE,2:NUMTWO,3:NUMTHREE,4:NUMFOUR,5:NUMFIVE,6:NUMSIX,7:NUMSEVEN,8:NUMEIGHT,9:NUMNINE,"dash":DASH}     

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

#Function to clear display by setting pixels to black
def cleardisplay():
    for x in range(w):
        for y in range(h):
            picounicorn.set_pixel(x, y, 0, 0, 0)            

#Function to update display with letters/numbers
def updatedisplay(displaymap):
    x=0
    y=0
    for row in displaymap: 
        for line in row:
            for char in line:
                if x < w and y <h:
                    if char == "X":
                        r, g, b = 255,255,255
                    elif char == "R":  
                        r, g, b = [int(c * 255) for c in hsv_to_rgb(x / w, y / h, 1.0)]
                    elif char == "D":
                        r, g, b = 200,200,40
                    elif char == "A":
                        r, g, b = playerABcolours
                    elif char == "Y":
                        r, g, b = playerXYcolours
                    else:
                        r,g,b=0,0,0
                    picounicorn.set_pixel(x, y, r, g, b)    
                x+=1
            x=0
        y+=1
    return displaymap

def update_scoreboard():    
    # Display team A's score
    for i in range(team_a_score):
        picounicorn.set_pixel(i, 0, 255, 0, 0)  # Set pixel color to red (team A)
   
    # Display team B's score
    for i in range(team_b_score):
        picounicorn.set_pixel(i, 6, 0, 0, 255)  # Set pixel color to blue (team B)
        
    #set turn for player A
        for i in range(player_a_turn):
        picounicorn.set_pixel(3, 6, 0, 0, 255)  # Set pixel color to blue (team B)
        
    #set turn for player X
        for i in range(player_a_turn):
        picounicorn.set_pixel(3, 19, 0, 0, 255)  # Set pixel color to blue (team B)    

def generatescore(scoreAB,scoreXY):
    scoreABpix = [item.replace("X","A") for item in scoredict[scoreAB]]
    scoreXYpix = [item.replace("X","Y") for item in scoredict[scoreXY]]
    dashpix = [item.replace("X","D") for item in scoredict["dash"]]
    fulldisplay = [["{}{}{}{}{}".format(BLANKSECTION[i],scoreABpix[i],dashpix[i],scoreXYpix[i],BLANKSECTION[i])] for i in range(h)]
    return fulldisplay

# Main loop
while True:

#Function to generate an 2D array to represent the current score in the format: PlayerABscore - PlayerXYscore
    currentdisplaymap=updatedisplay

    # Display the initial scoreboard
    update_scoreboard()
    
    # Check for button presses to update scores
    if picounicorn.is_pressed(picounicorn.BUTTON_A):
        team_a_score += 1
        time.sleep(0.2)  # Debounce the button press (adjust as needed)
    
    if picounicorn.is_pressed(picounicorn.BUTTON_B):
        team_b_score += 1
        time.sleep(0.2)  # Debounce the button press (adjust as needed)
    
    if picounicorn.is_pressed(picounicorn.BUTTON_X):
        team_a_score += 1
        time.sleep(0.2)  # Debounce the button press (adjust as needed)
    
    if picounicorn.is_pressed(picounicorn.BUTTON_Y):
        team_b_score += 1
        time.sleep(0.2)  # Debounce the button press (adjust as needed)