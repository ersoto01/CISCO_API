import requests

access_token = 'Mzc3YzY2MjAtZDRhOS00NjA5LWFmZDAtMDY4MGNjNDFiZTk4MmJjOTk0NGUtOGQ1_P0A1_4324cf20-3dc3-4497-af07-1b996464c625'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vNmNiZjYwODAtMzhmMC0xMWViLWE2YmEtZjM1ZTBhOTQ2MGQ0'

url = 'https://webexapis.com/v1/memberships'

header = {
    'Authorization' : 'Bearer {}'.format(access_token),
    'Content-Type' : 'application/json'
}
params = {
    'roomId' : room_id
}
resp = requests.get(url,headers = header,params=params)
print(resp.json())
