from random import randint


name = input("What is your name? ")
minimum = 1
maximum = 10

while name != "":
    lucky_number = randint(minimum, maximum)
    message = f"Hello {name}, your lucky number is {lucky_number}"
    if lucky_number == 3 or lucky_number == 9:
        message += " and you have won a prize"
    elif lucky_number == 7:
        message += " and you have hit the jackpot"
    print(message)
    print()
    name = input("What is your name? ")

print()
input("Press return to continue ...")
