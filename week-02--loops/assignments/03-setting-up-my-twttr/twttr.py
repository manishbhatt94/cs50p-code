def main():
    msg = input("Input: ").strip()
    print("Output:", strip_vowels(msg))


def strip_vowels(msg):
    vowels = ["a", "e", "i", "o", "u"]
    msg_sans_vowels = ""

    for char in msg:
        if char.lower() not in vowels:
            msg_sans_vowels += char

    return msg_sans_vowels


main()
