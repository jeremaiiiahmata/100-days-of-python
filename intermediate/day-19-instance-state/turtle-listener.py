from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

screen.setup(width=500,height=400)

def moveForward():
    turtle.forward(10)

def moveBackward():
    turtle.backward(10)

def rotateClockwise():
    turtle.right(10)

def rotateCounterClockwise():
    turtle.left(10)

def clearScreen():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

userInput = screen.textinput("Choose one!", "are you a NIGGA?")

print(userInput)

screen.listen()

screen.onkey(key="w", fun=moveForward)
screen.onkey(key="a", fun=rotateCounterClockwise)
screen.onkey(key="s", fun=moveBackward)
screen.onkey(key="d", fun=rotateClockwise)
screen.onkey(key="c", fun=clearScreen)


screen.exitonclick()