from turtle import Screen
from pong import Pong
import time
from paddle1 import Paddle1
from paddle2 import Paddle2
from boundry import Boundry
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)


pong = Pong()
paddle1 = Paddle1()
paddle2 = Paddle2()
boundry = Boundry()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle1.up, "w")
screen.onkeypress(paddle1.down, "s")
screen.onkeypress(paddle2.up, "Up")
screen.onkeypress(paddle2.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)
    pong.move_ball()

    # Detect collision with wall.
    if pong.xcor() > 290 or pong.xcor() < -290:
        if pong.heading() == 45:
            pong.setheading(315)
        elif pong.heading() == 315:
            pong.setheading(45)
        elif pong.heading() == 135:
            pong.setheading(225)
        elif pong.heading() == 225:
            pong.setheading(135)

screen.exitonclick()
