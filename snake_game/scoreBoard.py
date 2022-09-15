from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highScore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  Highscore: {self.highScore}", move=False, align="center", font=("Arial", 14, "normal"))

    def score_count(self):
        self.score += 1
        self.update_scoreboard()


    def updateHighscore(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("data.txt") as data:
                data.write(f"{self.highScore}")
        self.score = 0
        self.update_scoreboard()
    #def game_over(self):
        #self.goto(0,0)
        #self.write("GAME OVER", move=False, align="center", font=("Arial", 14, "normal"))




