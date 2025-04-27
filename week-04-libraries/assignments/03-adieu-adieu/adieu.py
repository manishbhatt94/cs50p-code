import inflect

p = inflect.engine()


def main():
    names = get_names_input()
    for i in range(len(names)):
        greet_first_n_people(names, i + 1)


def get_names_input():
    names_list = []

    while True:
        try:
            name = input("Name: ")
        except EOFError:
            print()
            return names_list
        else:
            names_list.append(name)


def greet_first_n_people(people, n):
    print("Adieu, adieu, to", p.join(people[:n]))


main()
