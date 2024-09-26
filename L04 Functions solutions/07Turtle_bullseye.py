import turtle as t


def circle_at(x, y, r, colour):
    t.penup()
    t.goto(x, y - r)
    t.pendown()
    t.fillcolor(colour)
    t.begin_fill()
    t.setheading(0)
    t.circle(r)
    t.end_fill()


t.speed(0)
circle_at(0, 0, 100, "white")
circle_at(0, 0, 80, "black")
circle_at(0, 0, 60, "blue")
circle_at(0, 0, 40, "red")
circle_at(0, 0, 20, "yellow")
t.hideturtle()

t.exitonclick()

print()
input("Press return to continue ...")
