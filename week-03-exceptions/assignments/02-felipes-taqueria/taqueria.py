def main():
    place_order()


def place_order():
    menu_items_price = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }
    total_cost = 0
    while True:
        try:
            item = input("Item: ").strip().title()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        else:
            if item in menu_items_price:
                total_cost += menu_items_price[item]
                print(f"${round(total_cost, 2):.2f}")


main()
