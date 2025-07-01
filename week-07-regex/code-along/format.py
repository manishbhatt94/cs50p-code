import re

name = input("What's your name? ").strip()

# Capturing Groups
#   A | B           -> either A or B
#   (...)           -> a group
#   (?:...)         -> non-capturing version (i.e. just for grouping - doesn't capture)


# matches = re.search(r"^(.+),\s*(.+)$", name)

# if matches:
# last = matches.group(1)
# first = matches.group(2)
# last, first = matches.groups()
# name = f"{first} {last}"

# Using the new "Walrus operator" :=
if matches := re.search(r"^(.+),\s*(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")
