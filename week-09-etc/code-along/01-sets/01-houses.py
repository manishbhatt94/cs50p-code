"""
Concept 01 in Week 09 Etcetra
* Set data structure
Given a list of dicts that represent students with 'name' & 'house' as keys.
Find the unique 'house's that exist, given this list of students
"""

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

# Non-efficient approach without a `set`
# houses = []
# for student in students:
#     if student["house"] not in houses:
#         houses.append(student["house"])

houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)
