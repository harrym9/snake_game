from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 14, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.sety(280)
        self.user_score = 0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.user_score}  "
                       f"High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.user_score > self.high_score:
            self.high_score = self.user_score
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))
        self.user_score = 0
        self.update_score()

    def add_score(self):
        self.user_score += 1
        self.update_score()
