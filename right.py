from turtle import Turtle,Screen
# from ball import BALL

class RIGHT:
    def __init__(self):
        self.right_bar = Turtle()
        self.right_bar.speed("fastest")
        self.screen=Screen()
        self.right_side()
        self.screen.listen()


    def up(self):
        y = self.right_bar.ycor()
        self.right_bar.sety(y + 20)

    def down(self):
        y = self.right_bar.ycor()
        self.right_bar.sety(y - 20)

    def right_side(self):

        self.right_bar.shape('square')
        self.right_bar.color("gray")
        self.right_bar.penup()
        self.right_bar.shapesize(stretch_wid=4, stretch_len=1)
        self.right_bar.goto(-350, 0)

        self.screen.onkey(key="1", fun=self.up)
        self.screen.onkey(key="2", fun=self.down)




