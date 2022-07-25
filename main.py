from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)
snk = Snake()
food = Food()
scrboard = ScoreBoard()

screen.listen()
screen.onkey(snk.up, "w")
screen.onkey(snk.down, "s")
screen.onkey(snk.left, "a")
screen.onkey(snk.right, "d")
screen.onkey(snk.up, "Up")
screen.onkey(snk.down, "Down")
screen.onkey(snk.left, "Left")
screen.onkey(snk.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snk.move_snake()

    if snk.head.distance(food) < 15:
        food.refresh()
        snk.extend()
        scrboard.increase_score()

    if snk.head.xcor() > 280 or snk.head.xcor() < -280 or snk.head.ycor() > 280 or snk.head.ycor() < -280:
        scrboard.reset_highscore()
        snk.reset_snake()

    # Detect collision with tail.
    for segment in snk.segments:
        if segment == snk.head:
            pass
        elif snk.head.distance(segment) < 10:
            scrboard.reset_highscore()
            snk.reset_snake()

screen.exitonclick()
