from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 270)
        self.write(f"{self.score1} zu {self.score2}", align="center", font=("Arial", 12, "bold"))

    def keep_score1(self):
        self.score1 += 1
        self.clear()
        self.write(f"{self.score1} zu {self.score2}", align="center", font=("Arial", 12, "bold"))

    def keep_score2(self):
        self.score2 += 1
        self.clear()
        self.write(f"{self.score1} zu {self.score2}", align="center", font=("Arial", 12, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 12, "bold"))