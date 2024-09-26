from string import punctuation


def count_punctuation(s):
    """Return a count of the punctuation in s."""
    counter = 0
    for c in s:
        if c in punctuation:
            counter += 1
    return counter


from string import whitespace


def count_whitespace(s):
    """Return a count of the whitespace in s."""
    counter = 0
    for c in s:
        if c in whitespace:
            counter += 1
    return counter


def count_letters(s):
    """Return a count of the letters in s."""
    counter = 0
    for c in s:
        if c.isalpha():
            counter += 1
    return counter


def count_digits(s):
    """Return a count of the letters in s."""
    counter = 0
    for c in s:
        if c.isdigit():
            counter += 1
    return counter


string = "Hello, COMP1753!! How are you doing today?"

print(string)
print(f" {count_letters(string):4} letters")
print(f" {count_digits(string):4} digits")
print(f" {count_whitespace(string):4} whitespace characters")
print(f" {count_punctuation(string):4} punctuation marks")
print(f" {len(string):4} Total")

print()
input("Press return to continue ...")
