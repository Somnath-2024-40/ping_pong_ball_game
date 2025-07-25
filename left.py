from turtle import Turtle,Screen
# from ball import BALL

class LEFT:
    def __init__(self):
        self.left_bar = Turtle()
        self.left_bar.speed("fastest")
        self.screen=Screen()
        self.left_side()
        self.screen.listen()


    def up(self):
        y = self.left_bar.ycor()
        self.left_bar.sety(y + 20)

    def down(self):
        y = self.left_bar.ycor()
        self.left_bar.sety(y - 20)

    def left_side(self):

        self.left_bar.shape('square')
        self.left_bar.color("skyblue")
        self.left_bar.penup()
        self.left_bar.shapesize(stretch_wid=4, stretch_len=1)
        self.left_bar.goto(350,0)

        self.screen.onkey(key="w", fun=self.up)
        self.screen.onkey(key="s", fun=self.down)




