import requests
import json

access_token = 'Mzc3YzY2MjAtZDRhOS00NjA5LWFmZDAtMDY4MGNjNDFiZTk4MmJjOTk0NGUtOGQ1_P0A1_4324cf20-3dc3-4497-af07-1b996464c625'

url = 'https://webexapis.com/v1/rooms'

header = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type' : 'application/json'
}
params = {
    'title' : 'DevNet Associate Training'
}
resp = requests.post(url,headers = header,json=params)
print(json.dumps(resp.json(), indent = 4))

