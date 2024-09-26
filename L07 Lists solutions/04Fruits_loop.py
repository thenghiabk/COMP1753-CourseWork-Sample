def print_list(items, header=None):
    if header != None:
        print(header)
    for item in items:
        print(f"{item}")
    print()


fruits = []

while True:
    fruit = input("Guess another fruit? ")
    if fruit in fruits or fruit == "":
        break
    fruits.append(fruit)

print()
print_list(fruits, "FRUITS")
print(f"Your score is {len(fruits)}")

print()
input("Press return to continue ...")
