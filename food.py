import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed("fastest")
        self.penup()
        self.shapesize(0.5)
        self.color("red")
        self.new_food()

    def new_food(self):
        xcor = random.randint(-280,280)
        ycor = random.randint(-280,280)
        self.goto(xcor,ycor)