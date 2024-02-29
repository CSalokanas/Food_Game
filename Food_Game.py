from turtle import Screen
from Player import Create_Player
from Score_Board import Scoreboard
from Food_dropping import Food
from Level import Level
from playsound import playsound
from level_up_text import Level_up_text
from Lives import Lives_board

# Create a list of food objects
foods_list = [Food(), Food(), Food(), Food(), Food()]
# Creates leveling system
level = Level()

# Create a scoreboard object
ScoreBoard = Scoreboard()

# Create a player object
Player1 = Create_Player()

# Specify the background picture file
BackGround_Picture = "pictures/background-picture.png"

lives = Lives_board()

# Create a screen object
Main_Screen = Screen()
Main_Screen.bgcolor("black")
Main_Screen.bgpic(picname=BackGround_Picture)
Main_Screen.title("Food Game")
Main_Screen.setup(width=800, height=578)

# Listen for keyboard input
Main_Screen.listen()

# Assign keyboard events to player's movement functions
Main_Screen.onkey(fun=Player1.go_left, key="a")
Main_Screen.onkey(fun=Player1.go_right, key="d")
# Set the game state as 'on'
Game_is_on = True
playsound("Sounds/countdown.mp3", block=True)
# Game loop
counter = 0
while Game_is_on:

    player_x = Player1.xcor()
    # Iterate through each food drop in the list
    for food_drop in foods_list:

        # Make the food drop
        food_drop.food_dropping()
        food_drop.name
        
        # Check if player and food collide
        if Player1.distance(x=food_drop.xcor(), y=food_drop.ycor()) <= 35:
            if food_drop.name == "heart":
                lives.Lives += 1
                lives.update_lives()
            if food_drop.name == "speedboost":
                Player1.player_speed += 5
            if food_drop.name == "bomb":
                Game_is_on = False
                ScoreBoard.game_over()
                playsound("Sounds/loosing_sound.mp3", block=False)
            if food_drop.healthy:
                # If the food is healthy, refresh it and update the score
                food_drop.refresh()
                playsound("Sounds/eating_healthy_sound.mp3", block=False)
                ScoreBoard.score += 1
                ScoreBoard.update_scoreboard()
                level.xp += 1
                level.update_level()
                if ScoreBoard.score > int(ScoreBoard.high_score):
                    ScoreBoard.high_score = ScoreBoard.score
                    ScoreBoard.update_scoreboard()
            else:
                # If the food is unhealthy, refresh it and decrease the score
                food_drop.refresh()
                playsound("Sounds/eating_unhealthy_sound.mp3", block=False)
                ScoreBoard.score -= 1
                ScoreBoard.update_scoreboard()
                level.xp -= 2
                level.update_level()
        # Check if the food drop reaches the bottom of the screen
        if food_drop.ycor() < -260:
            food_drop.refresh()
        # Check if the score is negative, end the game
        if ScoreBoard.score < 0:
            lives.Lives -= 1
            lives.update_lives()
            if lives.Lives == 0:
                ScoreBoard.game_over()
                playsound("Sounds/loosing_sound.mp3", block=False)
            Game_is_on = False

        # Check if the score reaches the winning condition, end the game
        if ScoreBoard.score >= 50:
            ScoreBoard.game_won()
            playsound("Sounds/win.mp3")

            Game_is_on = False
        if ScoreBoard.score in {5,10,15, 20, 25, 30, 35, 40, 45}:
            food_drop.food_dropping_speed += 1

        if level.xp == level.level_up:
            counter += 1
            playsound("Sounds/level.mp3", block=False)
            BackGround_Picture = f"pictures/{counter}.png"
            Level_up_text(player_x=player_x)
            level.level_up1()
            level.update_level()


# Exit the game when the screen is clicked
Main_Screen.exitonclick()
