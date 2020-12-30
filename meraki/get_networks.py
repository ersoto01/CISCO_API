import requests
import json

# Organizacion KB, ID = 959854

url = "https://dashboard.meraki.com/api/v0/organizations/959854/networks"

payload={}
headers = {
  'X-Cisco-Meraki-Api-Key': 'fa6edf53121f528e4d60b5064c1c57a986b94796'
}

response = requests.get(url, headers=headers, data=payload).json()
print(json.dumps(response,indent= 2, sort_keys=True))
'''
for temp1 in response:
  if temp1["name"] == "OC":
    net_id = temp1["id"]

print (net_id)
'''