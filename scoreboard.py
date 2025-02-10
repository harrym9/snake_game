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

    def show_score(self):
        self.write(arg=f"Score: {self.user_score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.user_score += 1
        self.clear()

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER!", align=ALIGNMENT, font=FONT)