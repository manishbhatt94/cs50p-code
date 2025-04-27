import random


def main():
    level = get_level()
    score = 10

    for _ in range(10):
        num1 = generate_integer(level)
        num2 = generate_integer(level)
        problem_solved = False
        for _ in range(3):
            try:
                response = int(input(f"{num1} + {num2} = "))
            except ValueError:
                continue
            if response == num1 + num2:
                problem_solved = True
                break
            else:
                print("EEE")
        if not problem_solved:
            score -= 1
            print(f"{num1} + {num2} = {num1 + num2}")

    print("Score:", score)


def get_level():
    while True:
        try:
            num = int(input("Level: "))
        except ValueError:
            continue
        else:
            if 1 <= num <= 3:
                return num


def generate_integer(level):
    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)
        case _:
            raise ValueError


if __name__ == "__main__":
    main()
