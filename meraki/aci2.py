import requests
import json

url = "https://sandboxapicdc.cisco.com:443/api/aaaLogin.json"

payload = {
    "aaaUser": {
            "attributes": {
                "name":"admin",
                "pwd":"ciscopsdt"
            }
        }
}
headers = {
  'Content-Type': 'application/json'
}

response = requests.post(url, data = json.dumps(payload),headers=headers, verify=False).json()

#print(response)
#print(response['imdata'][0]['aaaLogin']['attributes']['token'])
token = response['imdata'][0]['aaaLogin']['attributes']['token']
#print(token)



url= "https://sandboxapicdc.cisco.com/api/node/class/fvTenant.json"
header = {
           "Cookie" : f"APIC-Cookie={token}"
           }
response = requests.get(url, headers=header, verify=False)
response_json = response.json()
tenants = response_json['imdata']
#print(tenants)
for tenant in tenants:
    #print(tenant)
    print(f"Nombre de Tenant: {tenant['fvTenant']['attributes']['name']}")