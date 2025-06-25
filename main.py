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

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
scoreboard = Scoreboard()
ball = Ball()

screen.listen()
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")
screen.onkeypress(r_paddle.move_up, "l")
screen.onkeypress(r_paddle.move_down, ",")

delay = 0.05

game_over = False
while not game_over:
    time.sleep(delay)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() <= -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        delay -= 0.001

    if ball.xcor() > 380 or ball.xcor() < -380:
        if ball.xcor() > 380:
            scoreboard.left_point()
        else:
            scoreboard.right_point()
        ball.reset_ball()
        delay = 0.05
        time.sleep(1)

screen.exitonclick()