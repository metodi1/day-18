import random
from turtle import Turtle, Screen

colors = ["light sky blue", "yellow green", "firebrick", "gold", "dark green", "magenta"]
tim = Turtle()
tim.shape("turtle")
tim.pendown()
start_pen_size = 5
tim.speed("fastest")
move = [0, 90, 180, 270]



for turns in range(110):
    tim.pensize(start_pen_size)
    tim.pencolor(random.choice(colors))
    tim.forward(11)
    tim.setheading(random.choice(move))

screen = Screen()
screen.exitonclick()
