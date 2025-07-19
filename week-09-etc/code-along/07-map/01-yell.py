"""
Concept 07 in Week 09 Etcetra

* -> Pass list
* Pass variable number of arguments
* `map` function
* List Comprehension


Write a function `yell` that takes in string(s) and prints uppercased versions
"""

"""
Approach 01 - Pass a list of strings to `yell`
"""


def main():
    yell(["This", "is", "CS50"])


def yell(words: list[str]) -> None:
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


if __name__ == "__main__":
    main()
