def first(items):
    return items[0]


def last(items):
    return items[len(items)-1]


fruits = ["Banana","Orange","Apple","Mango"]

print(first(fruits))
print(last(fruits))

fruits.sort()

print()
print(first(fruits))
print(last(fruits))

fruits.reverse()

print()
print(first(fruits))
print(last(fruits))

print()
input("Press return to continue ...")
