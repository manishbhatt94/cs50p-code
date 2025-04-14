from typing import Tuple


def main():
    while True:
        date_input = input("Date: ").strip()
        date_parts = parse_date_from_format_1(date_input) or parse_date_from_format_2(
            date_input
        )
        if date_parts is not None:
            print(format_date_iso8601(*date_parts))
            break


def format_date_iso8601(year: int, month: int, day: int) -> str:
    """
    Given year, month, day as parameters, this function returns a string which
    represents that date but formatted in ISO-8601 format i.e. "YYYY-MM-DD"
    """
    return f"{year:04}-{month:02}-{day:02}"


def parse_date_from_format_1(date_str: str) -> None | Tuple[int, int, int]:
    """
    Parse a string `date_str` of the format "MM/DD/YYYY"
    Returns a tuple of the parsed components of the date i.e. (year, month, day)
    If failed to parse, then returns None
    """
    try:
        month, day, year = date_str.split("/")
        month = int(month.strip())
        day = int(day.strip())
        year = int(year.strip())
    except ValueError:
        return None
    else:
        if (not 1 <= month <= 12) or (not 1 <= day <= 31):
            return None
        return year, month, day


def parse_date_from_format_2(date_str: str) -> None | Tuple[int, int, int]:
    """
    Parse a string `date_str` of the format "January 26, 1950"
    Returns a tuple of the parsed components of the date i.e. (year, month, day)
    If failed to parse, then returns None
    """
    valid_months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    try:
        rest, year = date_str.split(",")
        month, day = rest.strip().split(" ")
        year = int(year.strip())
        day = int(day)
    except ValueError:
        return None
    else:
        if month not in valid_months or (not 1 <= day <= 31):
            return None
        month_num = valid_months.index(month) + 1
        return year, month_num, day


main()
