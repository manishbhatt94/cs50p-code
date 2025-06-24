students = []

with open("v1-students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(
            {
                "name": name,
                "house": house,
            }
        )


# def get_name(student):
#     return student["name"]

# sort list of dictionaries by a particular 'key'
# for student in sorted(students, key=get_name):
#     print(f"{student['name']} is in {student['house']}")


for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
