from turtle import Turtle


class Boundary(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(-400, -300)
        self.pendown()
        self.goto(-400, 300)
        self.goto(400, 300)
        self.goto(400, -300)
        self.goto(-400, -300)
