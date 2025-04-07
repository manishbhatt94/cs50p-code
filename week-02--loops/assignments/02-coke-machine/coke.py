# coke selling price: 50c
# machine accepts following denominations:
# 25c, 10c, 5c


def main():
    accepted_denominations = [5, 10, 25]
    amount_to_collect = 50
    collect_payment(amount_to_collect, accepted_denominations)


def collect_payment(amount_to_collect, accepted_denominations):
    while amount_to_collect > 0:
        print("Amount Due:", amount_to_collect)
        coin_received = int(input("Insert Coin: ").strip())
        if coin_received not in accepted_denominations:
            continue
        amount_to_collect -= coin_received

    print("Change Owed:", abs(amount_to_collect))


main()
