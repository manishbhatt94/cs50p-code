import random


class Hat:
    # class (static) variable 'houses'
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    # class (static) method 'sort'
    @classmethod
    def sort(cls, name):
        # ^^^^^ instead of 'self', 1st param is 'cls' which is reference to the current class
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")
