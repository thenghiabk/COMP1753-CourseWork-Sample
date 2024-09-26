from random import randint


fruits = ["Banana","Orange","Apple","Mango"]

name = input("What is your name? ")

print(f"Hello {name}, your lucky fruit is {fruits[randint(0, len(fruits))]}")

print()
input("Press return to continue ...")
