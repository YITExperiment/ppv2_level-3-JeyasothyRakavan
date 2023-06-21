import turtle

from itertools import cycle
colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

def draw_cycle(size,angle,shift):
    turtle.bgcolor(colors)
    turtle.pencolor(colors)
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_cycle(size+5, angle+1, shift+1)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(40)
draw_cycle(30,0,1)
