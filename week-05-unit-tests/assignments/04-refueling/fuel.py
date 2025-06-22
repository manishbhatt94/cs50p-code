def main():
    fuel_percent = get_fuel_percent("Fraction: ")
    print(gauge(fuel_percent))


def get_fuel_percent(input_prompt):
    while True:
        frac_str = input(input_prompt).strip()
        try:
            percent = convert(frac_str)
        except (ValueError, ZeroDivisionError) as err:
            print(err)
            continue
        else:
            return percent


def convert(fraction):
    frac_parts = fraction.split("/")
    if len(frac_parts) != 2:
        raise ValueError("Invalid Fraction: Missing '/' character")
    x = int(frac_parts[0].strip())
    y = int(frac_parts[1].strip())
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError("Invalid Fraction: Not a proper fraction")
    return round((x * 100) / y)


def gauge(percentage):
    if percentage <= 1:
        level = "E"
    elif percentage >= 99:
        level = "F"
    else:
        level = f"{percentage}%"
    return level


if __name__ == "__main__":
    main()
