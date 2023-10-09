from picounicorn import PicoUnicorn
picounicorn = PicoUnicorn()
import time

w = picounicorn.get_width()  # 16
h = picounicorn.get_height()  # 7

# Define team scores
team_a_score = 0
team_b_score = 0

# Define digit representations (0-9)
digits = [
    [0b111, 0b101, 0b101, 0b101, 0b111],  # 0
    [0b010, 0b010, 0b010, 0b010, 0b010],  # 1
    [0b111, 0b001, 0b111, 0b100, 0b111],  # 2
    [0b111, 0b001, 0b111, 0b001, 0b111],  # 3
    [0b101, 0b101, 0b111, 0b001, 0b001],  # 4
    [0b111, 0b100, 0b111, 0b001, 0b111],  # 5
    [0b111, 0b100, 0b111, 0b101, 0b111],  # 6
    [0b111, 0b001, 0b001, 0b001, 0b001],  # 7
    [0b111, 0b101, 0b111, 0b101, 0b111],  # 8
    [0b111, 0b101, 0b111, 0b001, 0b111]   # 9
]

def display_digit(x, y, digit):
    for row, pattern in enumerate(digits[digit]):
        for col in range(3):
            if pattern & (1 << col):
                picounicorn.set_pixel(x + col, y + row, 255, 255, 255)  # Set pixel color to white

def update_scoreboard():
    # Display team A's score
    display_digit(0, 0, team_a_score)
    
    # Display team B's score
    display_digit(8, 0, team_b_score)

# Main loop
while True:
    # Display the initial scoreboard
    update_scoreboard()
    
    # Check for button presses to update scores
    if picounicorn.is_pressed(picounicorn.BUTTON_A):
        team_a_score += 1
        if team_a_score > 9:
            team_a_score = 0
        time.sleep(0.2)  # Debounce the button press (adjust as needed)
    
    if picounicorn.is_pressed(picounicorn.BUTTON_B):
        team_b_score += 1
        if team_b_score > 9:
            team_b_score = 0
        time.sleep(0.2)  # Debounce the button press (adjust as needed)
