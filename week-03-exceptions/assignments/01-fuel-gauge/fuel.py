def main():
    print(get_fuel_level())


def get_fuel_level():
    # Take fuel level as a fraction from user input
    x, y = get_proper_fraction()
    fuel_percent = round((x * 100) / y)
    if fuel_percent <= 1:
        level = "E"
    elif fuel_percent >= 99:
        level = "F"
    else:
        level = f"{fuel_percent}%"
    return level


def get_proper_fraction():
    while True:
        frac_parts = input("Fraction: ").strip().split("/")
        if len(frac_parts) != 2:
            continue
        try:
            x = int(frac_parts[0].strip())
            y = int(frac_parts[1].strip())
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if x > y:
                continue
            return x, y


main()
