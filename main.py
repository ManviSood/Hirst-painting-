import colorgram
from turtle import Turtle, Screen
import turtle as t
import random

hirst = Turtle()

screen = Screen()

t.colormode(255)

colors = colorgram.extract('image.jpg', 20)

print(f"{colors} \n")

# for i in range(len(colors)):
#     first_color = colors[i]
#     rgb = first_color.rgb
#     print(rgb)

my_tuple = []

hirst.speed("fastest")


def draw_dots(value):
    hirst.pencolor(value)
    hirst.pensize(8)
    hirst.dot()
    hirst.penup()
    hirst.fd(30)
    return


# Reset the position
def reset_pos(dist):
    hirst.home()
    hirst.sety(dist)
    return dist + 30


for i in range(len(colors)):
    first_color = colors[i]
    rgb = (first_color.rgb.r, first_color.rgb.g, first_color.rgb.b)
    my_tuple.append(rgb)

print(my_tuple)

n_rows = int(input("Enter no. of rows you want: "))
n_columns = int(input("Enter no. of columns you want: "))

i = 0
is_continue = 0
dist_y = 30
while is_continue < n_columns:
    if i < n_rows:
        print(random.choice(my_tuple))
        draw_dots(random.choice(my_tuple))
        i += 1
    else:
        dist_y = reset_pos(dist_y)
        i = 0
        is_continue += 1

screen.exitonclick()
