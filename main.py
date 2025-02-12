import time
from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
from snake import Snake

X_COR = 600
Y_COR = 600
WALLS_FOR_X_COR = (Y_COR // 2) - 10
WALLS_FOR_Y_COR = (Y_COR // 2) - 10

screen = Screen()
screen.tracer(0)
screen.setup(X_COR, Y_COR)
screen.bgcolor("black")
screen.title("Snake Game")

score = ScoreBoard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    score.update_score()
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.new_food()
        snake.extend()
        score.add_score()

    # Detect collision with wall
    if (snake.head.xcor() >= WALLS_FOR_X_COR or snake.head.xcor() <= -WALLS_FOR_X_COR or
            snake.head.ycor() >= WALLS_FOR_Y_COR or snake.head.ycor() <= -WALLS_FOR_Y_COR):
        score.reset_score()
        snake.reset_snake()

    # Detect collision with segment:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_score()
            snake.reset_snake()

screen.exitonclick()
