"""
Concept 07 in Week 09 Etcetra

* "filter" function

Syntax:
filter(function, iterable)

=========

Filter a list of students to only those whose "house" is "Gryffindor"
"""

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]


def main():
    gryffindors = filter(is_gryffindor, students)
    # gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

    for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
        print(gryffindor["name"])


def is_gryffindor(student):
    return student["house"] == "Gryffindor"


if __name__ == "__main__":
    main()
