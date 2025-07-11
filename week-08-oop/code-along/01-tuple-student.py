def main():
    student = get_student()
    if student[0] == "Padma":
        # Tuples, unlike Lists, are immutable
        student[1] = (
            "Ravenclaw"  # Raises TypeError: 'tuple' object does not support item assignment
        )
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    # return name, house  # Implicit tuple (without parenthesis)
    return (name, house)  # Explicit tuple (wrapped with parenthesis)


if __name__ == "__main__":
    main()
