import re


def main():
    print(convert(input("Hours: ")))


def convert(s: str) -> str:
    s = s.strip()
    pattern = r"^(\d{1,2}(?::\d{2})?) ([AP]M) to (\d{1,2}(?::\d{2})?) ([AP]M)$"

    if match := re.search(pattern, s):
        start = parse_12hrs_time(match.groups()[:2])
        end = parse_12hrs_time(match.groups()[2:])
        validate_12hrs_time(start)
        validate_12hrs_time(end)
        return f"{format_time_24hrs(start)} to {format_time_24hrs(end)}"
    else:
        raise ValueError("Input format is invalid")


# def parse_12hrs_time(matched_time: tuple[str, Literal["AM", "PM"]]):
def parse_12hrs_time(matched_time):
    time, ampm = matched_time
    if ":" in time:
        hours, mins = map(int, time.split(":"))
    else:
        hours, mins = int(time), 0
    return (hours, mins, ampm)


# def validate_12hrs_time(time: tuple[int, int, Literal["AM", "PM"]]):
def validate_12hrs_time(time):
    hours, mins = time[:2]
    if (hours < 1 or hours > 12) or (mins < 0 or mins > 59):
        raise ValueError("Time is invalid")


# def format_time_24hrs(time: tuple[int, int, Literal["AM", "PM"]]):
def format_time_24hrs(time):
    hours, mins, ampm = time
    if ampm == "PM" and hours != 12:
        hours += 12
    elif ampm == "AM" and hours == 12:
        hours = 0
    return f"{hours:02}:{mins:02}"


if __name__ == "__main__":
    main()
