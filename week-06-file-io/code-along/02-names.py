name = input("What's your name? ")

print(f"hello, {name}")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
