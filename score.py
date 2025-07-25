from turtle import Turtle

class SCORE:
    def __init__(self):
        self.right_score=Turtle()
        self.left_score=Turtle()
        self.s1=0
        self.s2=0
        for t in (self.right_score,self.left_score):
            t.speed("fastest")
            t.color("white")
            t.penup()
            t.hideturtle()
        self.left_score.goto(-300, 250)
        self.right_score.goto(300, 250)
        self.update_score()

    def update_score(self):
        self.left_score.clear()
        self.right_score.clear()
        self.left_score.write(f"score: {self.s1}", align="center", font=("Arial", 16, "bold"))
        self.right_score.write(f"score: {self.s2}", align="center", font=("Arial", 16, "bold"))

    def left_point(self):
        self.s1 += 1
        self.update_score()

    def right_point(self):
        self.s2 += 1
        self.update_score()





