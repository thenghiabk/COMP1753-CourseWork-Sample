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


def frequency(items):
    """Return count of each item in list of items."""
    count = {}
    for item in items:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    return count


string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "\
    "Proin sit amet nulla scelerisque, ultrices enim sed, pretium mi. "\
    "Aenean neque orci, maximus quis risus quis, blandit rutrum purus. "\
    "Etiam varius dui eget justo tempor elementum. "\
    "Duis finibus felis a dapibus tincidunt. "\
    "Nam quis dui tempus, tristique tortor a, vehicula odio. "\
    "Sed ac dolor vel augue imperdiet placerat. "\
    "Donec malesuada erat sapien, molestie convallis nisl iaculis a. "\
    "Donec turpis mi, tincidunt at dolor sit amet, pulvinar commodo justo. "\
    "Proin rutrum nisl et sollicitudin tincidunt. "\
    "Maecenas ut diam ac justo consectetur tincidunt. "\
    "Phasellus pulvinar lectus ut orci finibus aliquam. "\
    "Cras sit amet urna laoreet, aliquet ipsum ut, vulputate odio. "\
    "Vestibulum consectetur, tortor et consectetur gravida, dui nulla dapibus mauris, ac dapibus metus neque nec odio. "\
    "Aliquam at molestie ipsum."
string = string.lower()
string = remove_punctuation(string)
string = remove_whitespace(string)

characters = list(string)

count = frequency(characters)

print("CHARACTER FREQUENCY - sorted by decreasing frequency")
sorted_keys = sorted(count, key=count.get)
sorted_keys.reverse()
for key in sorted_keys:
    print(f"{count.get(key):3} {key}")
print()

print()
input("Press return to continue ...")
