import re


def main():
    print(parse(input("HTML: ").strip()))


def parse(s: str):
    pattern = r"src=\"https?://(?:www\.)?youtube\.com/embed/(?P<video_id>\w{11})\""

    if not (s.startswith("<iframe ") and s.endswith("</iframe>")):
        return None

    if matches := re.search(pattern, s):
        return f"https://youtu.be/{matches.group('video_id')}"
    else:
        return None


if __name__ == "__main__":
    main()
