import random
from turtle import Turtle, Screen

colors = ["light sky blue", "yellow green", "firebrick", "gold", "dark green", "magenta"]
tim = Turtle()
tim.shape("turtle")
tim.pendown()
start_pen_size = 30


def draw_shape():
    turns = movements()
    angle = 360 / turns
    for _ in range(turns):
        tim.forward(100)
        tim.right(angle)


def movements():
    UP = 0
    DOWN = -100
    LEFT = -90
    RIGHT = 90
    move = [UP, DOWN, LEFT, RIGHT]
    next_move = random.choice(move)
    return next_move


for turns in range(3, 11):
    start_pen_size -= 2
    tim.pensize(start_pen_size)
    draw_shape()
    tim.pencolor(random.choice(colors))

screen = Screen()
screen.exitonclick()
