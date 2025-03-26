

def convert(message: str):
  """
  Takes a `message` (str) as parameter.
  Returns `message`, but with the following 2 emoticons, replaced with their
  corresponding emojis:
  :) => 🙂
  :( => 🙁
  """
  converted = message.replace(":)", "🙂").replace(":(", "🙁")
  return converted


def main():
  # Take a message as input from user
  msg = input("Enter a message to emojify: ")
  emojified = convert(msg)
  print(emojified)


main()
