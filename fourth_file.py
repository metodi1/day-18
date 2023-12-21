import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)


def rondom_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    color = (r, g, b)

    return color


tim = Turtle()
tim.shape("turtle")
tim.pendown()
start_pen_size = 9
tim.speed("fastest")
move = 0


def draw_spirograph(step):
    rounds = int(360/step)
    for turns in range(rounds):
        tim.pencolor(rondom_color())
        tim.circle(50)
        tim.setheading(tim.heading()+step)


draw_spirograph(5)


screen = Screen()
screen.exitonclick()
