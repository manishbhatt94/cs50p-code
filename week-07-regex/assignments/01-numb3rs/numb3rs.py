import re


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip: str) -> bool:
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"

    if matches := re.search(pattern, ip):
        return all(octet_valid(octet) for octet in matches.groups())
    else:
        return False


def octet_valid(octet: str) -> bool:
    # leading zero invalid case
    if len(octet) > 1 and octet.startswith("0"):
        return False
    # range check
    if int(octet) > 255:
        return False
    return True


if __name__ == "__main__":
    main()
