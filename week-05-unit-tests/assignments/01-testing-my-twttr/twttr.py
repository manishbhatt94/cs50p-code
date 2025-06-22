def main():
    msg = input("Input: ").strip()
    print("Output:", shorten(msg))


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    chars = list(word)
    short_msg = "".join([ch for ch in chars if ch.lower() not in vowels])

    return short_msg


if __name__ == "__main__":
    main()
