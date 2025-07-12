import random


# Note that: static members are different than class members in Python
# and have a separate annotation called `@staticmethod` (separate from `@classmethod`)
# TODO: Research about "static" members in Python, & how they differ from "class" members
class Hat:
    # class variable 'houses'
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    # class method 'sort'
    @classmethod
    def sort(cls, name):
        # ^^^^^ instead of 'self', 1st param is 'cls' which is reference to the current class
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")
