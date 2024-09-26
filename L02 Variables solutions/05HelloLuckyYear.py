from random import randint


name = input("What is your name? ")
year_of_birth = input("What is your year of birth? ")
lucky_year = int(year_of_birth) + randint(0, 70)
print(f"Hello {name}, your lucky year is {lucky_year}")

print()
input("Press return to continue ...")
