import csv
import sys

from tabulate import tabulate


def main():
    path = get_filepath_from_cmdargs()
    menu = read_menu(path)
    print_formatted_menu(menu)


def get_filepath_from_cmdargs():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    path = sys.argv[1]

    if not path.endswith(".csv"):
        sys.exit("Not a CSV file")

    return path


def read_menu(menu_filepath):
    try:
        menu = []
        with open(menu_filepath, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                menu.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        return menu


def print_formatted_menu(menu):
    print(tabulate(menu, headers="firstrow", tablefmt="grid"))


if __name__ == "__main__":
    main()
