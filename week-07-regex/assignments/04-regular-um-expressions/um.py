import re


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\bum\b"

    if found := re.findall(pattern, s, flags=re.IGNORECASE):
        return len(found)
    else:
        return 0


if __name__ == "__main__":
    main()
