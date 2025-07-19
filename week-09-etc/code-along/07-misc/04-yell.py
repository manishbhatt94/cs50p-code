"""
Concept 07 in Week 09 Etcetra

* Pass list
* Pass variable number of arguments
* `map` function
* -> List Comprehension


Write a function `yell` that takes in string(s) and prints uppercased versions
"""

"""
Approach 04 - Using "List Comprehension"
"""


def main():
    yell("This", "is", "CS50")


def yell(*words: str) -> None:
    uppercased = [word.upper() for word in words]
    print(*uppercased)


if __name__ == "__main__":
    main()
