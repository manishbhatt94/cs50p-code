"""
Concept 07 in Week 09 Etcetra

* `enumerate` function

=========

Given a list of students' names,
Print the students' names alongwith their rank
Rank here just means position in the list
"""

students = ["Hermione", "Harry", "Ron"]

"""Approach 02 - Using `enumerate` function"""


def main():
    for i, student in enumerate(students):
        print(i + 1, student)


"""Approach 01 - Without using `enumerate` function"""
# def main():
#     for i in range(len(students)):
#         print(i + 1, students[i])


if __name__ == "__main__":
    main()
