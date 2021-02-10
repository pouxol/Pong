from turtle import Turtle

Y_POSITIONS = [-30, -10, 10, 30]


class Paddle1:
    def __init__(self):
        self.segments = []
        self.create_paddle()

    def create_paddle(self):
        for position in Y_POSITIONS:
            t = Turtle()
            t.penup()
            t.shape("square")
            t.color("white")
            t.setpos(-380, position)
            self.segments.append(t)

    def up(self):
        for segment in self.segments:
            segment.setheading(90)
            segment.forward(10)

    def down(self):
        for segment in self.segments:
            segment.setheading(270)
            segment.forward(10)
