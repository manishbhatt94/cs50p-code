"""
Concept 03 in Week 09 Etcetra
* Constants

For declaring a constant inside a class, convention is to use a "class variable"
named in all uppercase
"""


class Cat:
    MEOWS_COUNT = 3  # class variable - used as a constant

    def meow(self):
        # Note: Inside instance methods, we access class variables using
        # ClassName.class_variable_name
        for _ in range(Cat.MEOWS_COUNT):
            print("meow")


cat = Cat()
cat.meow()
