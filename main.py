from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


food = Food()
snake = Snake()
score_board = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

#  Check if collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.new_score()
        snake.extend()

# Detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        score_board.reset()
        snake.reset()

# Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()
# If head collides with any segment in the tail: Trigger game_over











screen.exitonclick()
