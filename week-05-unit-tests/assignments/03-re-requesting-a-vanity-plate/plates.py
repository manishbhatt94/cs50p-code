def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[:2].isalpha():
        return False
    if not s.isalnum():
        return False
    return is_numeric_part_valid(s)


def is_numeric_part_valid(s):
    first_num_index = len(s)
    for i in range(len(s)):
        if s[i].isdigit():
            first_num_index = i
            break

    expected_numeric_part = s[first_num_index:]

    # no digits is valid
    if len(expected_numeric_part) == 0:
        return True

    # if digits are present, first digit must not be zero
    if expected_numeric_part[0] == "0":
        return False

    # digits are only allowed at the end
    return expected_numeric_part.isnumeric()


if __name__ == "__main__":
    main()
