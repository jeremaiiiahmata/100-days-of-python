from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "pink", "pale violet red"]

turtle.pensize(5)

def drawPolygon(sides):
    angle = 360/sides
    for steps in range(sides):
        turtle.right(angle)
        turtle.forward(100)


for i in range(3, 11):
    turtle.color(colors[i-3])
    drawPolygon(i)

screen.exitonclick()