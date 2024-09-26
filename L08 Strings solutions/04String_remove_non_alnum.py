def remove_non_alnum(s):
    """Return copy of s with whitespace & punctuation removed."""
    for c in s:
        if not c.isalnum():
            s = s.replace(c, "")
    return s


string = "Hello, world!! How are you doing today?"

print(string)
print(remove_non_alnum(string))

print()
input("Press return to continue ...")
