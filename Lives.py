from turtle import Turtle

class Lives_board(Turtle):
    def __init__(self):
        super().__init__()
        self.Lives = 1  # Initializing the number of lives
        self.penup()
        self.setpos(y=250, x=330)  # Positioning the lives display on the screen
        self.color("black")
        # Displaying the initial number of lives
        self.write(arg=f"Lives: {self.Lives}", move=False, align="center", font=('Arial', 16, 'normal'))
        self.hideturtle()  # Hide the turtle object as only the text is needed

    def update_lives(self):
        self.clear()  # Clear the previous lives display
        # Update and display the current number of lives
        self.write(arg=f"Lives: {self.Lives}", move=False, align="center", font=('Arial', 16, 'normal'))

