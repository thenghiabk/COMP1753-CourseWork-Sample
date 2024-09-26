# draw two squares, side by side, not touching

import turtle as t


def draw_square(length):
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)


draw_square(100)

t.penup()
t.forward(150)
t.pendown()

draw_square(75)

t.penup()
t.forward(125)
t.pendown()

draw_square(50)

t.penup()
t.forward(100)
t.pendown()

draw_square(25)

t.exitonclick()

print()
input("Press return to continue ...")
