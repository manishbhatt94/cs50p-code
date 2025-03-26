prompt_message = "What is the Answer to the Great Question of Life, the Universe, and Everything? "
response = input(prompt_message).strip().lower()

match response:
  case "42" | "forty-two" | "forty two":
    print("Yes")
  case _:
    print("No")

