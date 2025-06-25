from turtle import Turtle

FONT = ("Courier", 60, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center" ,font=FONT)
        self.goto(0, 200)
        # draw net?
        self.goto(100, 200)
        self.write(self.right_score, align="center" ,font=FONT)

    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()

