import random


def main():
    chosen_max = read_positive_int("Level: ")
    chosen_random_num = random.randint(1, chosen_max)

    while True:
        guessed_num = read_positive_int("Guess: ")
        if guessed_num > chosen_random_num:
            print("Too large!")
        elif guessed_num < chosen_random_num:
            print("Too small!")
        else:
            print("Just right!")
            break


def read_positive_int(prompt_msg):
    while True:
        try:
            num = int(input(prompt_msg))
        except ValueError:
            continue
        else:
            if num > 0:
                return num


main()
