import csv

students = []

# Using csv.DictReader to read rows as dict instead of list
# and keep keys as the header row of the CSV file

with open("v3-students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})


for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
