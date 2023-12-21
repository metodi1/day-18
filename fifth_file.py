import turtle

from colorgram import colorgram
from turtle import Turtle, Screen
import random

colors = colorgram.extract('image.jpg', 100)
tim = Turtle()
tim.speed("slow")
turtle.colormode(255)
rgb_colors = list()

d = len(colors)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
turn = 0


def draw_dot():
    tim.pendown()
    tim.dot(20, random.choice(rgb_colors))
    tim.penup()


tim.penup()
for a in range(0, 9):
    for b in range(0, 9):
        tim.forward(40)
        draw_dot()

    if a % 2 == 0:
        tim.setheading(90)
        tim.forward(40)
        tim.setheading(180)

    else:
        tim.setheading(90)
        tim.forward(40)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()
