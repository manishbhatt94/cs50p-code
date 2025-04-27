import random
import sys

from pyfiglet import Figlet

program_usage = """
Usage:
python3 figlet.py
(For rendering input text in a random font.)

OR

python3 figlet.py -f [font_name]
python3 figlet.py --font [font_name]
(For rendering input text in font: font_name.)
"""

args_num_incorrect_err_msg = f"""
Incorrect number of arguments received.
{program_usage}
"""


def main():
    figlet = Figlet()
    available_fonts = figlet.getFonts()

    match len(sys.argv):
        case 1:
            selected_font = random.choice(available_fonts)
        case 3:
            flag, selected_font = sys.argv[1:]
            if flag not in ["-f", "--font"] or selected_font not in available_fonts:
                sys.exit("Invalid usage")
        case _:
            sys.exit("Invalid usage")

    text = input("Input: ")
    figlet.setFont(font=selected_font)
    print(figlet.renderText(text))


main()
