# Side effect
# Changing a global variable


emoticon = "v.v"


def main():
    """main function demonstrates how to change the value of a global variable
    from within a function using global keyword
    """
    global emoticon
    say("Is anyone there?")
    emoticon = ":D"
    say("Oh, hi!")


def say(phrase):
    print(phrase + " " + emoticon)


main()
