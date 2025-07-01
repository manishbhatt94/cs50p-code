import re

url = input("Your Twitter Profile URL: ").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

print(f"Username: {username}")
