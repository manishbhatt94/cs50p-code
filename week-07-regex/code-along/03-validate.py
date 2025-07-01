import re

# re standard library -- intro

email = input("What's your email? ").strip()

# Character Classes
# \w => [a-zA-Z0-9_] alpha-numeric-underscore set (including uppercase)

# More Character Classes
# \d    decimal digit
# \D    not a decimal digit
# \s    whitespace characters (like space tab etc)
# \S    not a whitespace character
# \w    word character ... as well as numbers & underscore
# \W    not a word character


# flags param in re.search(pattern, string, flags)
# accepts bitwise OR of any of following 3 possible flags
# re.IGNORECASE     - self explanatory
# re.MULTILINE      - allows newline character(s) within string
# re.DOTALL         - the "dot" special char includes newline char also


if re.search(r"^\w+@\w+\.edu$", email, flags=re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
