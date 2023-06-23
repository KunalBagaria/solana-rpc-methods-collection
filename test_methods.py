import requests
import json

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
    url = request['url']
    headers = {header['key']: header['value'] for header in request['header']}
    body = request['body']['raw']

    print(f"[{index + 1}/{len(items)}] Running {name} request...")
    response = requests.request(method, url, headers=headers, data=body)

    print("Response Status Code:", response.status_code)
    print("Response Content:", response.content, "\n")
