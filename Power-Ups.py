from turtle import Turtle, Screen
from random import choice, randint

# List of available power-ups
power_up_list = ["speedboost", "Extra Life", "Fruit Rain", "Smart Bomb"]

class Power_ups(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        # Randomly select a power-up from the power_up_list
        self.name = choice(power_up_list)
        # Set the shape of the power-up based on the selected name
        self.shape(f"{self.name}.png")
        self.speed(1)  # Set the drawing speed of the turtle
        # Randomly position the power-up on the screen
        self.goto(x=randint(-380, 380), y=randint(200, 400))
        self.dropping_speed = 5  # Speed at which the power-up will drop down the screen

