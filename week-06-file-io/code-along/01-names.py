name = input("What's your name? ")

print(f"hello, {name}")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
