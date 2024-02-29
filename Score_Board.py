from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0  # Initialize the score
        self.penup()
        self.setpos(y=250, x=0)  # Position the scoreboard on the screen
        # Open the high score file in read mode and read the high score
        file = open("high_score.txt", "r")  
        self.high_score = int(file.read().strip())  # Convert the high score to an integer
        file.close()  # Close the file
        self.color("black")
        # Display the initial score and high score
        self.write(arg=f"Score: {self.score}, high score: {self.high_score}", move=False, align="center",
                   font=('Arial', 16, 'normal'))
        self.hideturtle()  # Hide the turtle object, as we only need the text

    def update_scoreboard(self):
        # Update the high score in the file
        file = open("high_score.txt", "w")  
        file.write(str(self.high_score))
        file.close()
        self.clear()  # Clear the previous score
        # Display the updated score and high score
        self.write(arg=f"score: {self.score}, high score: {self.high_score}", move=False, align="center",
                   font=('Arial', 16, 'normal'))

    def game_over(self):
        # Display the game over message at the center of the screen
        self.goto(y=0, x=0)
        self.write(arg="Game is over", move=False, align="center", font=('Arial', 16, 'normal'))

    def game_won(self):
        # Display the game won message at the center of the screen
        self.goto(y=0, x=0)
        self.write(arg="You Won", move=False, align="center", font=('Arial', 16, 'normal'))

