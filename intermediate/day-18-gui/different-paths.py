import random
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "pink", "pale violet red"]
angles = [90, 180, 270, 360]

turtle.pensize(15)
turtle.speed("fastest")

while True:
    randomColor = random.choice(colors)
    angle = random.choice(angles)

    turtle.color(randomColor)
    turtle.forward(25)
    turtle.setheading(angle)


