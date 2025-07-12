"""
Getters & Setters for attributes of a class
using @property and @house.setter (or @<name-of-attribute>.setter) decorators
"""


class Student:
    def __init__(self, name, house):
        # setter is called even for the `self.name = name` assignment in __init__ as well
        self.name = name
        # setter is called even for the `self.house = house` assignment in __init__ as well
        self.house = house
        # ...
        # But assignment using `self._name = name` which uses the underlying
        # attribute (note the leading underscore) and not the property (or the @property) `name`
        # Such assignment does not call the setter, & is so (in our example) not validated.
        # ...
        # Similarly for `self._house = house`

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    # Below line - goes through setter - and is validated according to the code
    # we wrote in the setter - so it will lead to a ValueError("Invalid house")
    # student.house = "Number Four, Privet Drive"
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
