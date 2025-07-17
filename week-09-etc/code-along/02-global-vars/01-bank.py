"""
Concept 02 in Week 09 Etcetra
* Global Variables in Python

Taking a look at UnboundLocalError which arises when assigning to a global variable
from within a function
"""

balance = 0


def main():
    # Reading global variable `balance` is allowed
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    # Reading global variable `balance` is allowed
    print("Balance:", balance)
    # But, assigning to global variable `balance` is not allowed, as we see
    # from the UnboundLocalError in functions `deposit(n)` & `withdraw(n)`


def deposit(n):
    # Below runtime error:
    # UnboundLocalError: cannot access local variable 'balance' where it is not
    # associated with a value
    balance += n  # Ruff warning: Local variable `balance` referenced before assignment Ruff(F823)


def withdraw(n):
    # Below runtime error:
    # UnboundLocalError: cannot access local variable 'balance' where it is not
    # associated with a value
    balance -= n  # Ruff warning: Local variable `balance` referenced before assignment Ruff(F823)


if __name__ == "__main__":
    main()
