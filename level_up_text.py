from turtle import Turtle
from time import sleep

class Level_up_text(Turtle):
    def __init__(self, player_x):
        super().__init__()
        self.hideturtle()  # Hide the turtle as we only need it for text display
        self.penup()
        # Set the position of the text relative to the player's x-coordinate
        self.setpos(x=player_x, y=-230)
        # Display "LEVELED UP!" text
        self.write(arg=f"LEVELED UP!", move=False, align="center", font=('Arial', 10, 'normal'))
        sleep(1)  # Pause for 1 second to allow the text to be visible
        self.clear()  # Clear the text after 1 second

