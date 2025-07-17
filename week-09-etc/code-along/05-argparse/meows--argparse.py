"""
Concept 05 in Week 09 Etcetra
* argparse

Using "argparse" library
https://docs.python.org/3/howto/argparse.html

This program can be run like:

[prints help message]
python3 meows--argparse.py -h
python3 meows--argparse.py --help

[pass an int 'N' to option "-n"]
python3 meows--argparse.py -n N

[don't pass option "-n" at all - default value of 1 is applied]
python3 meows--argparse.py
"""

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", help="number of times to meow", type=int, default=1)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")
