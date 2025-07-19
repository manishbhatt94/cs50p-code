"""
Concept 07 in Week 09 Etcetra

* List Comprehension (for filtering)

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
    gryffindors = [
        student["name"] for student in students if student["house"] == "Gryffindor"
    ]
    for gryffindor in sorted(gryffindors):
        print(gryffindor)


if __name__ == "__main__":
    main()
