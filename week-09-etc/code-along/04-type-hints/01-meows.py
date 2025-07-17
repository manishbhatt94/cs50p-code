"""
Concept 04 in Week 09 Etcetra
* 1. Type Hints

Using Python package "mypy" (Installed using `pip install mypy`)
to perform static type checking

Run with:
`mypy 01-meows.py`


* 2. Docstrings
Use triple quotes.
Inside we can use a special markup format called reStructuredText (reST)
to specify params, their types, return type and etc in a formatted way
Refer:
https://devguide.python.org/documentation/markup/
https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
"""


def meow(n: int) -> str:
    """
    Meow n times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :returns: A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")
