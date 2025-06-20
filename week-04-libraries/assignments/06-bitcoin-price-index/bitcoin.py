import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()


def main():
    btc = read_btc_input()
    usd = get_usd_from_btc(btc)
    print(f"${usd:,.4f}")


def read_btc_input():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    try:
        amount_btc = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    return amount_btc


def get_usd_from_btc(amount_btc):
    api_key = os.getenv("COINCAP_API_KEY")
    if api_key is None:
        sys.exit("Provide COINCAP_API_KEY environment variable.")
    # api_key = "your-api-key"

    try:
        response = requests.get(
            f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"
        )
        response.raise_for_status()
        coincap_response_json = response.json()
    except (requests.HTTPError, requests.JSONDecodeError) as err:
        print(f"Error occurred: {err}")
        sys.exit("Failed to get BTC rate in USD")

    amount_usd = amount_btc * float(coincap_response_json["data"]["priceUsd"])
    return amount_usd


main()
