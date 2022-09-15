from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to Snake Game")
screen.tracer(0)

snake = Snake()
cake = Food()

Score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(cake) < 15:
        cake.refresh()
        Score.score_count()
        snake.extend()

    if snake.head.xcor() > 295 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -295:
       Score.updateHighscore()
       snake.reset()
    for block in snake.blocks[1:]:
        if snake.head.distance(block) <10:
            Score.updateHighscore()
            snake.reset()

















screen.exitonclick()