from turtle import Turtle


class Paddle2(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.setpos(380, 0)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
