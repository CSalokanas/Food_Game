from turtle import Turtle, Screen

# Registering a custom shape for the player character
Screen().register_shape("pictures/character-removebg-preview.gif", None)

# Setting initial position coordinates for the player
original_x = 0
original_y = -260

class Create_Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        # Setting the initial position of the player
        self.goto(x=original_x, y=original_y)
        # Setting the player's appearance using a custom image
        self.shape("pictures/character-removebg-preview.gif")
        self.speed(10)  # Setting the drawing speed of the turtle
        self.player_speed = 15  # Defining the movement speed of the player

    def go_right(self):
        # Moving the player to the right by a specified amount (player_speed)
        self.goto(x=self.xcor() + self.player_speed, y=original_y)

    def go_left(self):
        # Moving the player to the left by a specified amount (player_speed)
        self.goto(x=self.xcor() - self.player_speed, y=original_y)

