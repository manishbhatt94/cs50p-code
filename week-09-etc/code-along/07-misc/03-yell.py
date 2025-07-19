"""
Concept 07 in Week 09 Etcetra

* Pass list
* Pass variable number of arguments
* -> `map` function
* List Comprehension

`map` function allows us to map, i.e., apply some function to every element of
some sequence, like a list

Syntax:
map(function, iterable, ...)

=========

Write a function `yell` that takes in string(s) and prints uppercased versions
"""

"""
Approach 03 - Use the `map` function
"""


def main():
    yell("This", "is", "CS50")


def yell(*words: str) -> None:
    uppercased = map(str.upper, words)
    print(*uppercased)


if __name__ == "__main__":
    main()
