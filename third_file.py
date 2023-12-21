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
move = [0, 90, 180, 270]

for turns in range(50):
    tim.pencolor(rondom_color())
    tim.forward(11)
    tim.setheading(random.choice(move))

screen = Screen()
screen.exitonclick()
