from turtle import Screen
from pong import Pong
import time
from paddle1 import Paddle1
from paddle2 import Paddle2
from boundary import Boundary
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

pong = Pong()
paddle1 = Paddle1()
paddle2 = Paddle2()
boundary = Boundary()
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

    # Detect collision with wall and bounce.
    if int(pong.ycor()) == 293 or int(pong.ycor()) == -293:
        in_heading = pong.heading()
        if in_heading == 45:
            pong.setheading(315)
        elif in_heading == 315:
            pong.setheading(45)
        elif in_heading == 135:
            pong.setheading(225)
        elif in_heading == 225:
            pong.setheading(135)

    # Detect leaving boundary.
    if int(pong.xcor()) >= 400:
        scoreboard.keep_score1()
        time.sleep(1)
        pong.start_ball()
    elif int(pong.xcor()) <= -400:
        scoreboard.keep_score2()
        time.sleep(1)
        pong.start_ball()

    # Detect collision with paddle1 and bounce.
    if int(pong.distance(paddle1)) <= 60 and int(pong.xcor()) == -360:
        senf = 0
        while senf == 0:
            senf = 1
            in_heading = pong.heading()
            if in_heading == 225:
                pong.setheading(315)
            elif in_heading == 135:
                pong.setheading(45)

    # Detect collision with paddle2 and bounce
    if int(pong.distance(paddle2)) <= 60 and int(pong.xcor()) == 360:
        senf = 0
        while senf == 0:
            senf = 1
            in_heading = pong.heading()
            if in_heading == 315:
                pong.setheading(225)
            elif in_heading == 45:
                pong.setheading(135)

    # Finish Game
    if scoreboard.score1 == 5 or scoreboard.score2 == 5:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
