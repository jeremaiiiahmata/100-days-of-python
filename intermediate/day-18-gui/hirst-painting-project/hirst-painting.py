import colorgram
import turtle as t
import random
from colorlist import colors

turtle = t.Turtle()
screen = t.Screen()

t.colormode(255)

# ------ Colorgram
# def extractColors(numberOfColors):
#     colors = colorgram.extract("./image.jpg", numberOfColors)
#
#     colorPalette = []
#
#     for color in colors :
#         r = color.rgb.r
#         g = color.rgb.g
#         b = color.rgb.b
#
#         palette = (r,g,b)
#
#         colorPalette.append(palette)
#
#     return colorPalette
#
# colors = extractColors(30)
# print(colors)
# turtle.color(colors[0])
# turtle.dot(50, colors[0])

turtle.speed("fastest") #Sets the speed of the animation to fastest.

turtle.up() #Doesn't create a line when the turtle moves.
turtle.setposition(-250, -250) #Sets the initial position to the lower left side
y = -250

for i in range(10) :
    x = -250
    turtle.sety(y)
    print(turtle.pos())

    for i in range(10):
        turtle.setx(x)
        turtle.dot(25, random.choice(colors))\

        print(turtle.pos())

        x += 50

    y += 50

turtle.hideturtle()

screen.exitonclick()






