from turtle import Turtle

FONT = ("Arail", 50, "normal")
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 220)
        self.write(f"{self.l_score}", align="center", font=FONT)
        self.goto(100, 220)
        self.write(f"{self.r_score}", align="center", font=FONT)

    def l_count(self):
        self.l_score += 1
        self.update()

    def r_count(self):
        self.r_score += 1
        self.update()