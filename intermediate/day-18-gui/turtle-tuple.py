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

turtle.pensize(15)
turtle.speed("fastest")

while True:
    angle = random.choice(angles)

    turtle.color(randomColor())
    turtle.forward(25)
    turtle.setheading(angle)


