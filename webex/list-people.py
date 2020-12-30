import requests
import json

access_token = 'Mzc3YzY2MjAtZDRhOS00NjA5LWFmZDAtMDY4MGNjNDFiZTk4MmJjOTk0NGUtOGQ1_P0A1_4324cf20-3dc3-4497-af07-1b996464c625'

url = 'https://webexapis.com/v1/people'

header = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {
    'email': 'ernesto.soto@pucp.pe'
}

resp = requests.get(url, headers = header, params=params)
#print(json.dumps(resp.json(),indent = 4))

person_id = resp.json()['items'][0]['id']
#print('person_id:',person_id)

url_personId = 'https://webexapis.com/v1/people/{}'.format(person_id)
resp_personId = requests.get(url_personId,headers = header)
print(json.dumps(resp_personId.json(),indent = 4))

