from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Build the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Classic Pong Game")
screen.tracer(0)

ball = Ball()
scoreboard = Scoreboard()
user_paddle = Paddle(350, 0)
comp_paddle = Paddle(-350, 0)

screen.listen()
screen.onkeypress(user_paddle.up, "Up")
screen.onkeypress(user_paddle.down, "Down")
screen.onkeypress(comp_paddle.up, "w")
screen.onkeypress(comp_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect Collision with Edge
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect Collision with Paddle
    if (ball.distance(user_paddle) < 50 and ball.xcor() > 320) or \
            (ball.distance(comp_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Point for user
    if ball.xcor() > 400:
        scoreboard.comp += 1
        scoreboard.refresh()
        ball.point()

    # Point for comp
    if ball.xcor() < -400:
        scoreboard.user += 1
        scoreboard.refresh()
        ball.point()

screen.exitonclick()
