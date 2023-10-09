from picounicorn import PicoUnicorn
picounicorn = PicoUnicorn()
import time

w = picounicorn.get_width()#16
h = picounicorn.get_height()#7

# Define team scores
team_a_score = 0
team_b_score = 0

def update_scoreboard():    
    # Display team A's score
    for i in range(team_a_score):
        picounicorn.set_pixel(i, 0, 255, 0, 0)  # Set pixel color to red (team A)
   
    # Display team B's score
    for i in range(team_b_score):
        picounicorn.set_pixel(i, 6, 0, 0, 255)  # Set pixel color to blue (team B)

# Main loop
while True:

    # Display the initial scoreboard
    update_scoreboard()
    
    # Check for button presses to update scores
    if picounicorn.is_pressed(picounicorn.BUTTON_A):
        team_a_score += 1
        time.sleep(0.2)  # Debounce the button press (adjust as needed)
    
    if picounicorn.is_pressed(picounicorn.BUTTON_B):
        team_b_score += 1
        time.sleep(0.2)  # Debounce the button press (adjust as needed)
    
