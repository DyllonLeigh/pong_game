from turtle import Screen
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

player = Paddle()
# ai = Paddle()
# scoreboard = Scoreboard()
ball = Ball()

screen.listen()
screen.onkeypress(player.move_up, "w")
screen.onkeypress(player.move_down, "s")

game_over = False
while not game_over:
    # ball.move()
    screen.update()
    # time.sleep(1)

screen.exitonclick()