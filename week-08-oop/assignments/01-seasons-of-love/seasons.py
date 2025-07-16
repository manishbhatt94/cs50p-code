import sys
from datetime import date

from inflect import engine

p = engine()


def main():
    try:
        dob_str = input("Date of Birth: ").strip()
        dob = parse_iso_date_str(date_str=dob_str)
        today = date.today()
        msg = get_message(from_date=dob, to_date=today)
        print(msg)
    except ValueError:
        sys.exit("Invalid date")


def parse_iso_date_str(date_str):
    return date.fromisoformat(date_str)


def get_message(from_date, to_date):
    if from_date > to_date:
        raise ValueError
    diff = to_date - from_date
    mins_elapsed = round(diff.total_seconds() / 60)
    mins_words = p.number_to_words(mins_elapsed, andword="").capitalize()
    return f"{mins_words} {p.plural_noun('minute', mins_elapsed)}"


if __name__ == "__main__":
    main()
