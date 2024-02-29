from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0  # Initial level set to 0
        self.xp = 0  # Initial experience points set to 0
        self.level_up = (self.level + 1) * 5  # Experience points needed for next level
        self.penup()
        self.setpos(y=250, x=-280)  # Position the level display on the screen
        self.color("black")
        # Display the initial level and experience points required for next level
        self.write(arg=f"Level:{self.level}, Next level:{self.xp}/{self.level_up}", move=False, align="center", font=('Arial', 16, 'normal'))
        self.hideturtle()  # Hide the turtle object, as we only need the text

    def update_level(self):
        self.clear()  # Clear the previous level display
        # Update and display the current level and experience points
        self.write(arg=f"Level:{self.level}, Next level:{self.xp}/{self.level_up}", move=False, align="center", font=('Arial', 16, 'normal'))

    def level_up1(self):
        self.xp = 0  # Reset experience points to 0 upon leveling up
        self.level += 1  # Increase the level by 1
        self.level_up = (self.level + 1) * 5  # Recalculate experience points needed for the next level

