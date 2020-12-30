import requests
import json

# Organizacion KB, ID = 739153288842183142

url = "https://dashboard.meraki.com/api/v0/networks/L_739153288842206374/devices"

payload={}
headers = {
  'X-Cisco-Meraki-Api-Key': '16bb8ee967f6b964e170f79b8a47498779df5c4b'
}

response = requests.get(url, headers=headers, data=payload).json()
print(json.dumps(response,indent= 2, sort_keys=True))

