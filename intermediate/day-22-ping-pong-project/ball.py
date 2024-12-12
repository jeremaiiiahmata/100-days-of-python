from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.goto(0,0)
        self.penup()
        self.xMove = 10
        self.yMove = 10
        self.ballSpeed = 0.1

    def bounceUp(self):
        newX = self.xcor() + self.xMove
        newY = self.ycor() + self.yMove
        self.goto(newX, newY)


    def bounceY(self):
        self.yMove *= -1
        self.ballSpeed *= 0.9

    def bounceX(self):
        self.xMove *= -1
        self.ballSpeed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.ballSpeed = 0.1

