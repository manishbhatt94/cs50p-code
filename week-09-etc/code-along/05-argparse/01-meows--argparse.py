"""
Concept 05 in Week 09 Etcetra
* argparse

argparse - is a module, part of Python standard library. This helps in parsing
command-line arguments comfortably

This file shows what command-line argument parsing looks like if implemented w/o
any libraries
"""

import sys

if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("usage: meows--argparse.py")
