import turtle as t


choice = input("What shape would you like (square or triangle)? ")

if choice == "square":
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)

    t.exitonclick()

elif choice == "triangle":
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)

    t.exitonclick()

else:
    print("WARNING: your shape has not been recognised")

print()
input("Press return to continue ...")
