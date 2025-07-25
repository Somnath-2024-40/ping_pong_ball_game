from turtle import Turtle,Screen
from border import BORDER
from ball import BALL
from left import LEFT
from right import RIGHT
from score import SCORE

t=Turtle()
t.penup()
t.shape('square')
t.color('white')

screen=Screen()
# screen.tracer(0)
screen.bgcolor('black')
screen.screensize(300,300)


bor=BORDER()
bor.som()
score=SCORE()
# score.left_score()
# score.right_score()
left=LEFT()
left.left_side()
right=RIGHT()
right.right_side()
bullu=BALL()

def game_loop():
    bullu.move()
    if bullu.b.distance(right.right_bar) < 50 and bullu.b.xcor() < -330:
        bullu.b.setheading(180 - bullu.b.heading())
        score.left_point()
    if bullu.b.distance(left.left_bar) < 50 and bullu.b.xcor() > 330:
        bullu.b.setheading(180 - bullu.b.heading())
        score.right_point()
    screen.update()
    screen.ontimer(game_loop, 50)
game_loop()
screen.mainloop()
screen.exitonclick()