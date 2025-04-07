def main():
    print_column(3)
    print_row(3)
    print_square(4)


def print_row(width):
    print("?" * width)


def print_column(height):
    print("#\n" * height, end="")


def print_square(size):
    for _ in range(size):
        print_row(size)


main()
