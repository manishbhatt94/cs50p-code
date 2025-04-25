import random

cards = ["jack", "queen", "king"]


def main():
    # pick a random element from a list
    # print(random.choice(cards))

    # pick 'k' random elements from a list (with replacement)
    # print(random.choices(cards, k=2))

    # pick 'k' random elements from a list (without replacement)
    # print(random.sample(cards, k=2))

    # pick 'k' random elements from a list (with replacement)
    # but not with equal probabilities (but custom weighted probabilities)
    # print(random.choices(cards, weights=[75, 20, 5], k=2))

    # passing custom constant seed for predicatable output
    # this is helpful in debugging code that utilises randomness
    random.seed(0)
    print(random.choices(cards, k=2))


main()
