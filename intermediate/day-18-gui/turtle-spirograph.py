import random
import turtle as t

turtle = t.Turtle()
screen = t.Screen()


t.colormode(255)

def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = (r, g, b)

    return color



angles = [90, 180, 270, 360]

turtle.speed("fastest")

# while True:
    # angle = random.choice(angles)

def drawSpirograph(gapSize) :
    for rotation in range(int(360/gapSize)) :
        turtle.color(randomColor())
        turtle.setheading(turtle.heading() + 5)
        turtle.circle(100)

drawSpirograph(1)

screen.exitonclick()

