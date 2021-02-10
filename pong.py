from turtle import Turtle
import random

ANGLES = [45, 135, 225, 315]


class Pong(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.setpos(0, 0)
        self.start_ball()

    def start_ball(self):
        self.setheading(random.choice(ANGLES))

    def move_ball(self):
        self.forward(5)

