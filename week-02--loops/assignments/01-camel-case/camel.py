def main():
    var_name_camel_cased = input("camelCase: ").strip()
    var_name_snake_cased = from_camel_to_snake(var_name_camel_cased)
    print("snake_case:", var_name_snake_cased)


def from_camel_to_snake(camel_cased):
    snake_cased = ""

    for character in camel_cased:
        if character.isupper():
            snake_cased += "_" + character.lower()
        else:
            snake_cased += character

    return snake_cased


main()
