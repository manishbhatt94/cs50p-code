"""
Concept 07 in Week 09 Etcetra

* Dictionary (dict) Comprehension

=========

Given a list of students' names that are in house Gryffindor,
- prepare a list of dicts with {"name": <student-name>, "house": "Gryffindor"}
- prepare a dict with key-values as: {<student-name>: "Gryffindor"}
"""

students = ["Hermione", "Harry", "Ron"]

"""Constructing a dict - Using dict comprehension:"""


def main():
    # Using a plain loop:
    # gryffindors = []
    # for student in students:
    #     gryffindors.append({"name": student, "house": "Gryffindor"})
    gryffindors = {student: "Gryffindor" for student in students}
    print(gryffindors)


"""Constructing a list of dicts - Using list comprehension:"""
# def main():
#     gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
#     print(gryffindors)


"""Constructing a list of dicts - Using a plain loop:"""
# def main():
#     gryffindors = []
#     for student in students:
#         gryffindors.append({"name": student, "house": "Gryffindor"})
#     print(gryffindors)


if __name__ == "__main__":
    main()
