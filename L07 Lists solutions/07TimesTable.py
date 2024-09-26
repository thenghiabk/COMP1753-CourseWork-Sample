def print_list(items, header=None):
    if header != None:
        print(header)
    for item in items:
        print(f"{item}")
    print()


def even(items):
    return items[::2]


def odd(items):
    return items[1::2]


times_table = int(input("Which times table? "))

table = []
for counter in range(13):
    table.append(times_table * (counter))

print_list(even(table), f"The {times_table} times table - even values")
print_list(odd(table), f"The {times_table} times table - odd values")

print()
input("Press return to continue ...")
