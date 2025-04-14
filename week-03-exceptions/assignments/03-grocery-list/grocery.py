def main():
    grocery_items_qty_map = make_shopping_list()
    display_shopping_list(grocery_items_qty_map)


def make_shopping_list():
    items_qty_map = {}

    while True:
        try:
            item = input().strip().upper()
            items_qty_map[item] += 1
        except (EOFError, KeyboardInterrupt):
            print()
            return items_qty_map
        except KeyError:
            items_qty_map[item] = 1


def display_shopping_list(grocery_map: dict):
    grocery_items = sorted(grocery_map)
    for item in grocery_items:
        print(grocery_map[item], item)


main()
