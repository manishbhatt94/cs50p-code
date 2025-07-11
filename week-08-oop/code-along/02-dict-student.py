"""
Using dict to model a Student object
"""


def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")


def get_student():
    return {
        "name": input("Name: "),
        "house": input("House: "),
    }


if __name__ == "__main__":
    main()
