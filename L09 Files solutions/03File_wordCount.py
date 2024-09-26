import os
from string import punctuation


def remove_punctuation(s):
    """Return copy of s with punctuation removed."""
    for c in punctuation:
        if c in s:
            s = s.replace(c, "")
    return s


def read(filename):
    """Return contents of text file as a string."""
    with open(filename) as file:
        return file.read()


def index_and_count_words(dirname, root_path_length):
    filenames = os.listdir(dirname)
    for filename in filenames:
        path = dirname + "\\" + filename
        if os.path.isdir(path):
            index_and_count_words(path, root_path_length)
        elif path.endswith(".txt"):
            string = remove_punctuation(read(path))
           # print(string)
            print(f"{len(string.split()):5} words in {path[root_path_length:]}")


try:
    root_path = os.pardir
    if os.path.isdir(root_path):
        index_and_count_words(root_path, len(root_path) + 1)
except OSError as err:
    print(err)
    print("Stopping, can't access files.")

print()
input("Press return to continue ...")
