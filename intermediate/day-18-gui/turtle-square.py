from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen() #Comes from the turtle module

turtle.shape("turtle")

for i in range(4):
    turtle.forward(300)
    turtle.right(90)


turtle.pencolor()

screen.exitonclick()