from turtle import Screen
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
# screen.tracer(0)
# screen.update()

player = Paddle()
ai = Paddle()
scoreboard = Scoreboard()
ball = Ball()

screen.exitonclick()

# screen.listen()
# screen.onkey(test, "a")