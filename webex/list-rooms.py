import requests
import json

access_token = 'Mzc3YzY2MjAtZDRhOS00NjA5LWFmZDAtMDY4MGNjNDFiZTk4MmJjOTk0NGUtOGQ1_P0A1_4324cf20-3dc3-4497-af07-1b996464c625'

url = 'https://webexapis.com/v1/rooms'

header = {
    'Authorization' : 'Bearer {}'.format(access_token),
    'Content-Type' : 'application/json'
}

params = {
    'max' : '100'
}

resp = requests.get(url,headers=header,params = params)
#print(resp.json())
print(json.dumps(resp.json(),indent = 4))
for item in resp.json()['items']:
    #print(item['id'])
    url_roomId = 'https://webexapis.com/v1/rooms/{}'.format(item['id'])
    resp_delete = requests.delete(url_roomId)#,headers = header)
    print(resp_delete.status_code)

resp = requests.get(url,headers=header,params = params)
print(resp.json())
