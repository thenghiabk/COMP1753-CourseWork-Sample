from string import punctuation


def remove_punctuation(s):
    """Return copy of s with punctuation removed."""
    for c in punctuation:
        if c in s:
            s = s.replace(c, "")
    return s


from string import whitespace


def remove_whitespace(s):
    """Return copy of s with whitespace removed."""
    for c in whitespace:
        if c in s:
            s = s.replace(c, "")
    return s


while True:
    string = input("Input a string: ")
    if string == "":
        break
    print(f"character count = {len(string)}")
    print(f"   letter count = {len(remove_whitespace(remove_punctuation(string)))}")
    print(f"     word count = {len(string.split())}")

print()
input("Press return to continue ...")
