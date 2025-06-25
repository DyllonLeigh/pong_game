from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        # self.hideturtle()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.5, 0.5)
        self.goto(0,0)

