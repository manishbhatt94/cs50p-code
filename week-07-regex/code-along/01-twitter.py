url = input("Your Twitter Profile URL: ").strip()

username = url.removeprefix("https://twitter.com/")

print(f"Username: {username}")
