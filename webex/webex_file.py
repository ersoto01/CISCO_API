import requests
import json

access_token = 'Mzc3YzY2MjAtZDRhOS00NjA5LWFmZDAtMDY4MGNjNDFiZTk4MmJjOTk0NGUtOGQ1_P0A1_4324cf20-3dc3-4497-af07-1b996464c625'
url = 'https://webexapis.com/v1/people/me'

headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

resp = requests.get(url,headers=headers)
print(json.dumps(resp.json(),indent=4))

