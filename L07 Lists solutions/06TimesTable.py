def print_list(items, header=None):
    if header != None:
        print(header)
    for item in items:
        print(f"{item}")
    print()


times_table = int(input("Which times table? "))

table = []
for counter in range(13):
    table.append(times_table * (counter))

print_list(table, f"The {times_table} times table")

print()
input("Press return to continue ...")
