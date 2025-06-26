import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    path = sys.argv[1]

    if not path.endswith(".py"):
        sys.exit("Not a Python file")

    print(get_loc_count(path))


def get_loc_count(path):
    try:
        loc = 0
        with open(path, "r") as file:
            for line in file:
                trimmed = line.strip()
                if len(trimmed) > 0 and (not trimmed.startswith("#")):
                    loc += 1
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        return loc


if __name__ == "__main__":
    main()
