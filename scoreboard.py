from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open("highscore.txt", mode="r+") as file:
            high_score = file.read()
            self.high_score = int(high_score)


        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-10,280)
        self.write(f"Score: {self.score}  High Score {self.high_score}", align="center",font=("Courier", 14, "normal"), )
        self.hideturtle()
        self.update()
    def update(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score {self.high_score}", align="center", font=("Courier", 14, "normal"), )

    def reset(self):
        if self.score>self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update()
        with open("highscore.txt",mode="w") as file:
            file.write(str(self.high_score))


    def track(self):
        self.score +=1
        self.update()

