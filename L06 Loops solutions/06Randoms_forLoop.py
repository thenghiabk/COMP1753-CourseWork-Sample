from random import randint


minimum = int(input("Min: "))
maximum = int(input("Max: "))

n_randoms = int(input("How many random numbers? "))
output = ""
for counter in range(n_randoms):
    random = randint(minimum, maximum)
    if random == 7:
        continue
    if random == 0:
        output = "Bad luck, no random values for you"
        break
    output += f" {random}"
print(output)

print()
input("Press return to continue ...")
