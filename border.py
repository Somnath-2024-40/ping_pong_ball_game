from turtle import Turtle


class BORDER:
    def __init__(self):



        self.som()


    def som(self):
        positions=[0,40,80,120,160,200,250,-40,-80,-120,-160,-200,-250]
        for y in positions:
            block = Turtle()
            block.penup()
            block.speed('fastest')
            block.shape('square')
            block.color('white')
            block.goto(0,y)
