from turtle import Screen
from ball import Ball
from paddle import Paddle
from score import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

rightPaddle = Paddle((350, 0))
leftPaddle = Paddle((-350, 0))

rightScore = Scoreboard((100,250))
leftScore = Scoreboard((-100,250))

ball = Ball()

screen.listen()

# ---- Left Paddle
screen.onkey(key="w", fun=leftPaddle.goUp)
screen.onkey(key="s", fun=leftPaddle.goDown)

# ---- Right Paddle
screen.onkey(key="Up", fun=rightPaddle.goUp)
screen.onkey(key="Down", fun=rightPaddle.goDown)

gameRunning = True

while gameRunning:
    time.sleep(ball.ballSpeed)
    screen.update()
    ball.bounceUp()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()

    if ball.distance(rightPaddle) < 50 and ball.xcor() > 320 or ball.distance(leftPaddle) < 50 and ball.xcor() < -320 :
        ball.bounceX()

    if ball.xcor() > 380 :
        ball.reset()
        leftScore.increaseScore()
    elif ball.xcor() < -380:
        ball.reset()
        rightScore.increaseScore()


screen.exitonclick()