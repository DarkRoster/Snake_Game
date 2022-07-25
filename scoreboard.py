from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as file:
            contents = file.read()
            self.temp = int(contents.split(":")[1])
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | Highscore: {self.temp}", align="center", font=("Arial", 24, "normal"))

    def reset_highscore(self):
        if self.score > self.temp:
            self.temp = self.score
            with open("highscore.txt", "w") as file:
                file.write(f"Highscore:{self.temp}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
