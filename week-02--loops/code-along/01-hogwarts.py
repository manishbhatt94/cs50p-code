students = [
    {
        "name": "Hermione",
        "house": "Gryffindor",
        "patronus": "Otter",
    },
    {
        "name": "Harry",
        "house": "Gryffindor",
        "patronus": "Stag",
    },
    {
        "name": "Ron",
        "house": "Gryffindor",
        "patronus": "Jack Russell terrier",
    },
    {
        "name": "Draco",
        "house": "Slytherin",
        "patronus": None,
    },
]

for student in students:
    for key in student:
        print(key, student[key], sep=": ")
    print()
