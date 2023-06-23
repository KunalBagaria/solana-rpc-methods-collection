import requests
import json
import sys

with open('rpc_methods.json', 'r') as file:
    json_data = json.load(file)

items = json_data['item']

print("Available Methods:")
for index, item in enumerate(items):
    name = item['name']
    print(f"{index + 1}. {name}")
print(f"\nTotal Methods: {len(items)}\n")

for index, item in enumerate(items):
    name = item['name']
    request = item['request']
    method = request['method']
    # replaces devnet url with local validator
    url = request['url'].replace('https://api.devnet.solana.com', 'http://localhost:8899')
    headers = {header['key']: header['value'] for header in request['header']}
    body = request['body']['raw']

    print(f"[{index + 1}/{len(items)}] Running {name} request...")
    response = requests.request(method, url, headers=headers, data=body)

    print("Response Status Code:", response.status_code)
    if response.status_code != 200:
        print("Error: HTTP", response.status_code)
        sys.exit(1)
