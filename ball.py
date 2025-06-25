from turtle import Turtle
from random import Random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.5, 0.5)
        self.setheading(180)
        self.goto(0,0)

    def move(self):
        self.forward(10)