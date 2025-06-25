from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.goto(-390, 0)

    def move_up(self):
        self.goto(-390, self.ycor() + 20)

    def move_down(self):
        self.goto(-390, self.ycor() - 20)