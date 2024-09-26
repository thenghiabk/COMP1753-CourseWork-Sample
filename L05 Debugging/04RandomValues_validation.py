from random import randint


min_str = input("Min: ")
max_str = input("Max: ")
minimum = int(min_str)
Maximum = int(max_str)

if maximum > minimum:
    random1 = randint(minimum, maximum)
    random2 = randint(minimum, maximum)
    random3 = randint(minimum+ maximum)
    random4 = randint(minimum, maximum)
    random5 = randint(minimum, maximum)
    print(f"{random1} {random2} {random3} {random4}")
else
    print(f"{maximum} is less than {minimum}")

print()
input("Press return to continue ...")
