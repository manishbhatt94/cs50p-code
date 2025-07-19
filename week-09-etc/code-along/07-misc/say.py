"""Final lecture"""

import cowsay

#  sudo apt update && sudo apt install espeak-ng libespeak1 alsa-utils
import pyttsx3

engine = pyttsx3.init()
this = input("What's this? ")  # Enter "This was CS50" for nostalgia, lol
cowsay.cow(this)
engine.say(this)
engine.runAndWait()
