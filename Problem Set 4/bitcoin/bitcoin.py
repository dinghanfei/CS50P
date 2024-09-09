import sys
import requests
import json

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    # print(json.dumps(response.json(), indent=2))
    bpi = o["bpi"]
    usd_bpi = bpi["USD"]
    # print(usd_bpi["rate"])
    rate = float(usd_bpi["rate"].replace(',',''))
    coins = float(sys.argv[1])
    amount = rate * coins
    print(f"${amount:,.4f}")
except requests.RequestException:
    pass
except ValueError:
    pass


