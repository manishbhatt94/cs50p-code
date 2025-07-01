import re

# re standard library -- intro

email = input("What's your email? ").strip()

# Groups -> Stuff surrounded in parenthesis

if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$", email, flags=re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

# Mentions of other "re" library methods
# From Python documentation at
# https://docs.python.org/3/library/re.html#search-vs-match

"""
search() vs. match()
Python offers different primitive operations based on regular expressions:

re.match() checks for a match only at the beginning of the string

re.search() checks for a match anywhere in the string (this is what Perl does by default)

re.fullmatch() checks for entire string to be a match
"""
