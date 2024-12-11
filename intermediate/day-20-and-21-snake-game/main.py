
from turtle import *
from snake import Snake
import time



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()


while True:
    screen.update()
    time.sleep(0.1) #Screens update every 0.1 seconds

    snake.move() #Everytime the screen refreshes, the snake move by 20 steps.

    #----- Only executes when triggered
    screen.listen() #Listens for any key events
    screen.onkey(key="w", fun=snake.moveUp)
    screen.onkey(key="a", fun=snake.moveLeft)
    screen.onkey(key="s", fun=snake.moveDown)
    screen.onkey(key="d", fun=snake.moveRight)


screen.exitonclick()