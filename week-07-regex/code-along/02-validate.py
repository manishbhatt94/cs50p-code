import re

# re standard library -- intro

email = input("What's your email? ").strip()

# using r".." raw strings to specify regex patterns
# to make escaping literal chars easy

# . -> any single char
# + -> one or more of previous char

# =     .       -> any character except a newline
# =     *       -> 0 or more repitions
# =     +       -> 1 or more repitions
# =     ?       -> 0 or 1 repitions
# =     {m}     -> m repitions
# =     {m,n}   -> m-n repitions


# Match start & end with ^ and $ respectively
if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
