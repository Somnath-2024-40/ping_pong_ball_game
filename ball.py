from turtle import Turtle
t=True
from turtle import Turtle

class BALL:
    def __init__(self):
        self.b = Turtle()
        self.b.shape('circle')
        self.b.color('yellow')
        self.b.penup()
        self.b.setheading(45)

    def move(self):
        self.b.forward(10)

        # Bounce on top or bottom wall
        if self.b.ycor() > 280 or self.b.ycor() < -280:
            self.b.setheading(-self.b.heading())

        # Left and right wall bounce
        if self.b.xcor() > 360 or self.b.xcor() < -360:
            self.b.setheading(180 - self.b.heading())













