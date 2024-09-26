from random import randint


def random(minimum=1, maximum=100):
    return randint(minimum, maximum)


min_str = input("Min: ")
max_str = input("Max: ")
minimum = int(min_str)
maximum = int(max_str)

if maximum > minimum:
    random1 = random()
    random2 = random(minimum)
    random3 = random(minimum, maximum)
    random4 = random(minimum, maximum)
    print(f"{random1} {random2} {random3} {random4}")
else:
    print(f"{maximum} is less than {minimum}")

print()
input("Press return to continue ...")
