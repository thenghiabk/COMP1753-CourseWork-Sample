def print_list(items, header=None):
    if header != None:
        print(header)
    for item in items:
        print(f"{item}")
    print()


fruits = ["Banana","Orange","Apple","Mango"]

favourite = input("What is your favourite fruit? ")
fruits.insert(0, favourite)

least_favourite = input("What is your least favourite fruit? ")
fruits.append(least_favourite) # easiest way to add to end
# fruits.insert(len(fruits), least_favourite) # alternative way to add to end

print_list(fruits, "FRUITS, favourite first")

fruits.sort()

print_list(fruits, "FRUITS, sorted")

print()
input("Press return to continue ...")
