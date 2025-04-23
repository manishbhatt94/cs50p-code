# "https://itunes.apple.com/search?entity=song&limit=1&term=weezer"

import sys

import requests

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    f"https://itunes.apple.com/search?entity=song&limit=15&term={sys.argv[1]}"
)
# print(json.dumps(response.json(), indent=2))

response_json = response.json()
for result in response_json["results"]:
    print(result["trackName"])
