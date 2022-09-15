from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreBoard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("WELCOME TO PONG")
screen.tracer(0)

r_paddle = Paddle((375, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()
scoreBoard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

Game_on = True
while Game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 345 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.reset_position()
        scoreBoard.l_count()

    if ball.xcor() < -400:
        ball.reset_position()
        scoreBoard.r_count()










screen.exitonclick()

