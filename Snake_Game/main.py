import time
from turtle import Screen

from brain import Snake
from food import Food
from score_board import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
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

    # Collision with Food, distance() -- could be x and y or the turtle itself, food shapesize is 10 and 10 pixels
    if snake.head.distance(food) < 14:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect Collision with wall
    if snake.head.xcor() > 310 or snake.head.xcor() < -310 or snake.head.ycor() > 310 or snake.head.ycor() < -310:
        score.reset_scoreboard()
        snake.reset_game()
    # Detect Collision with tale
    for turtle in snake.all_turtles[1:]:
        if snake.head.distance(turtle) < 14:
            score.reset_scoreboard()
            snake.reset_game()


screen.exitonclick()