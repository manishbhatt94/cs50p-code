"""
Concept 06 in Week 09 Etcetra
* Unpacking

Unpacking function's positional arguments
"""


def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]

print(total(*coins), "Knuts")
