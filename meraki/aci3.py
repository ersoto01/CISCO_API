import requests
import json

url= "https://sandboxapicdc.cisco.com/api/node/class/fvTenant.json"
header = {
           "Cookie" : f"APIC-Cookie={token}"
           }
response = requests.get(url, headers=header, verify=False)
response_json = response.json()
tenants = response_json['imdata']