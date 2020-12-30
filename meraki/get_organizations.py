import requests
import json

url = "https://dashboard.meraki.com/api/v0/organizations"

payload={}
headers = {
  'X-Cisco-Meraki-Api-Key': 'fa6edf53121f528e4d60b5064c1c57a986b94796'
}

response = requests.get(url, headers=headers, data=payload).json()

print(json.dumps(response,indent= 3))
print(response[0]["id"])