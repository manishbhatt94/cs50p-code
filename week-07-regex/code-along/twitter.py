import re

url = input("Your Twitter Profile URL: ").strip()

# Using non-capturing versions of Groups
# (?:...)
# So that only the group we're interested in (i.e. the username) gets captured

if matches := re.search(
    r"^(?:https?://)?(?:www\.)?twitter\.com/(\w+)", url, re.IGNORECASE
):
    print(f"Username: {matches.group(1)}")
