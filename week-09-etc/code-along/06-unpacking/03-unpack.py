"""
Concept 06 in Week 09 Etcetra
* Variadic functions
Functions that can take variable (multiple) no. of parameters
Using *args, **kwargs

->  *args       - as param indicates that this function takes
a variable number of "positional arguments"
                - Received as a tuple in the function

->  **kwargs    - as param indicates that this function takes
a variable number of "keyword arguments" or named paramaters
that can be called optionally & individually by their own name
                - Received as a dict in the function

"""


def f(*args, **kwargs):
    # print("Positional:", args)
    print("Named:", kwargs)


# f(100, 50, 25)
f(galleons=100, sickles=50, knuts=25)
