from turtle import Turtle, Screen
from random import randint, choice
from Food_Collection import food_collection, keys_array

# Registering custom shapes for different food items as turtle shapes
Screen().register_shape('pictures/apple.gif', None)
Screen().register_shape('pictures/banana.gif', None)
Screen().register_shape('pictures/broccoli.gif', None)
Screen().register_shape('pictures/carrot.gif', None)
Screen().register_shape('pictures/spinach.gif', None)
Screen().register_shape('pictures/salad.gif', None)
Screen().register_shape('pictures/chicken.gif', None)
Screen().register_shape('pictures/rice.gif', None)
Screen().register_shape('pictures/avocado.gif', None)
Screen().register_shape('pictures/pizza.gif', None)
Screen().register_shape('pictures/burger.gif', None)
Screen().register_shape('pictures/chocolate.gif', None)
Screen().register_shape('pictures/cake.gif', None)
Screen().register_shape('pictures/speedboost.gif', None)
Screen().register_shape('pictures/heart.gif', None)
Screen().register_shape('pictures/bomb.gif', None)


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.healthy = False
        # Randomly choosing a food item from the keys_array
        self.name = choice(keys_array)
        # Determining if the chosen food is healthy based on food_collection
        self.healthy = food_collection.get(self.name)
        # Setting the shape of the turtle to the chosen food item
        self.shape(f"pictures/{self.name}.gif")
        self.penup()
        # Randomly positioning the food item on the screen
        self.goto(x=randint(-380, 380), y=randint(200, 400))
        self.speed(1)
        # Setting the speed at which the food item will drop down the screen
        self.food_dropping_speed = 5

    def food_dropping(self):
        # Moving the food item downwards on the screen
        self.goto(x=self.xcor(), y=self.ycor() - self.food_dropping_speed)

    def refresh(self):
        # Refreshing the food item by choosing a new one and repositioning it
        self.name = choice(keys_array)
        self.healthy = food_collection.get(self.name)
        self.shape(f"pictures/{self.name}.gif")
        self.speed(0)
        self.goto(x=randint(-380, 380), y=200)
        self.speed(1)

