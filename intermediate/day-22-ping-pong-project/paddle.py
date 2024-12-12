from turtle import Turtle

class Paddle(Turtle) :

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def goUp(self):
        yCoordinate = self.ycor() + 20
        self.goto(self.xcor(), yCoordinate)

    def goDown(self):
        yCoordinate = self.ycor() - 20
        self.goto(self.xcor(), yCoordinate)