from turtle import *
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)
startingPos = [(0, 0), (-20, 0), (-40, 0)]
snake = []
x = 0


for pos in startingPos:
    block = Turtle("square")
    block.color("white")
    block.penup()

    block.goto(pos)

    snake.append(block)

def moveUp():
    snake[0].setheading(90)

def moveLeft():
    snake[0].setheading(180)

def moveDown():
    snake[0].setheading(270)

def moveRight():
    snake[0].setheading(0)




while True:
    screen.update()
    time.sleep(0.1) #Waits for 0.1 seconds before updating again.

    for each in range(len(snake)-1, 0, -1): #Sets the position of the next block to the current block, so it will be able to follow
        x = snake[each-1].xcor()
        y = snake[each-1].ycor()
        snake[each].setpos(x,y)

    #----- Only executes when triggered
    screen.listen() #Listens for any key events
    screen.onkey(key="w", fun=moveUp)
    screen.onkey(key="a", fun=moveLeft)
    screen.onkey(key="s", fun=moveDown)
    screen.onkey(key="d", fun=moveRight)

    snake[0].forward(20) #The front block of the snake moves forward by 20 blocks.
    #The consecutive blocks will follow the first block because of the for loop earlier (where the position of the block next to it will be the its new position)




screen.exitonclick()