name = input("What's your name? ").strip()

# For the case, user enters name as "<Lastname>, <Firstnam>"
if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"

print(f"hello, {name}")
