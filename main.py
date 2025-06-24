from turtle import Screen

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)


def test():
    print("a")

screen.listen()
screen.onkey(test, "a")

screen.update()

screen.exitonclick()