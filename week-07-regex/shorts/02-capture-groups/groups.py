import re

locations = {"+1": "United States and Canada", "+62": "Indonesia", "+505": "Nicaragua"}


def main():
    # pattern = r"(\+\d{1,3}) \d{3}-\d{3}-\d{4}"

    # Named Capture Groups using
    # (?P<some_name>)
    pattern = r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    number = input("Number: ")

    match = re.search(pattern, number)
    if match:
        country_code = match.group("country_code")
        print(locations[country_code])
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
