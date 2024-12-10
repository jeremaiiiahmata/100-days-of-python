from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "violet"]
steps = [10,15,20,25]
y_pos = [-70, -40, -10, 20, 50, 80]
turtles = []

for each in range(6):
    turtle = Turtle(shape="turtle")
    turtle.penup()

    turtle.color(colors[each])
    turtle.goto(-230, y_pos[each])

    turtles.append(turtle)


userBet = screen.textinput("WELCOME TO THE TURTLE RACE", "What color will win?")

if userBet :
    isGameOver = False

while not isGameOver:

    for turtle in turtles :
        turtleColor = turtle.pencolor()
        turtle.forward(random.choice(steps))

        if turtle.xcor() > 180 :
            print(f"{turtleColor.title()} turtle has won the race!")

            if userBet.lower() == turtleColor:
                print("You won!")
            else :
                print("Aww, man! Try again next time!")

            isGameOver = True

screen.exitonclick()


