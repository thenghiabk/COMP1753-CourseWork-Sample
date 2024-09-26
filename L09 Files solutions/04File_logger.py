import os


try:
    file = open("log.txt", "w")
    counter = 0
    while True:
        string = input("Please enter a string: ")
        if string == "":
            break
        file.write(string + "\n")
        counter += 1
    file.close()
    print(f"{counter} lines written to log.txt")
except OSError as err:
    print(err)
    print("Stopping, can't access log.txt.")

print()
input("Press return to continue ...")
