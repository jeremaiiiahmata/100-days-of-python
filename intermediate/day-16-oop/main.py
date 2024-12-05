# import turtle
from turtle import Turtle, Screen

# timmy = turtle.Turtle() <---- when using 'import turtle'

distance = 100

timmy = Turtle()
myScreen = Screen()
print("Initalizing...")

timmy.shape("turtle")
timmy.color("coral")
print("Changed color to coral")

choice = input("Move forward? Type 'y' for yes or 'n' for no :")

if choice.lower() == 'y':
    timmy.forward(distance)
    print(f"Moved forward to {distance}")

color = input("What is your favorite color? : ")


timmy.color(color)
print(f"Changed color to {color}")


myScreen.exitonclick()