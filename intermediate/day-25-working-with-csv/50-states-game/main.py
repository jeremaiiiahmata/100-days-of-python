from os import error
from turtle import Screen, Turtle
import pandas

screen = Screen()
image = "blank_states_img.gif"
screen.bgpic(image)
data = pandas.read_csv("./50_states.csv")
states = data["state"].to_list()

guessedStates = []

while len(guessedStates) < 50 :
    answer = screen.textinput(title=f"{len(guessedStates)}/50 States", prompt="Enter a state name :" )

    if answer.title() in states:
        #Creates a turtle with the name on the x,y coordinates of the state
        coordinates = data[data["state"] == answer.title()]
        turtle = Turtle()
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(coordinates.x.item(), coordinates.y.item())
        turtle.write(answer.title())

        guessedStates.append(answer)

screen.exitonclick()