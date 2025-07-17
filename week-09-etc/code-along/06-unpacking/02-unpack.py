"""
Concept 06 in Week 09 Etcetra
* Unpacking

Unpacking dictionary and pass its values as keyword args to function
"""


def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = {"galleons": 100, "sickles": 50, "knuts": 25}

# print(total(galleons=100, sickles=50, knuts=25), "Knuts")

print(total(**coins), "Knuts")  # Note the 2 stars `**`
