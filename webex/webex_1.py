import requests
import json

token = 'NDAxZGRlNGMtMWVmZC00ZDhjLThkMTUtMjUyNTFkYmVhZWZlNTAyYWY5MGEtM2Ni_P0A1_4324cf20-3dc3-4497-af07-1b996464c625'

url = 'https://api.ciscospark.com/v1/teams'
headers = {
            'Authorization': 'Bearer NDAxZGRlNGMtMWVmZC00ZDhjLThkMTUtMjUyNTFkYmVhZWZlNTAyYWY5MGEtM2Ni_P0A1_4324cf20-3dc3-4497-af07-1b996464c625',
            'Content-Type': 'application/json'
}
#print(json.dumps(headers))
#body = {
#    'name':'CBT Team'
#}
#post_response = requests.post(url,headers=headers,data=json.dumps(body)).json()
#print(post_response)

#get_response = requests.get(url,headers=headers).json()
#teams = get_response['items']
#for team in teams:
#    if team['name'] == 'CBT Team':
#        teamId = team['id']

#print(teamId)

###### create a room ###########
room_url = 'https://api.ciscospark.com/v1/rooms'
#room_body = {
#    'title': 'CBT_Room',
#    'teamId': teamId
#}
#room_post = requests.post(room_url,headers=headers,data=json.dumps(room_body)).json()
#print(room_post)

get_rooms = requests.get(room_url, headers = headers).json()
rooms = get_rooms['items']
for room in rooms:
    if room['title']=='CBT_Room':
        room_Id = room['id']

print(room_Id)

##### create a message ###############
msg_url = 'https://api.ciscospark.com/v1/messages'
msg_body = {
   'roomId' : room_Id,
   'text' : 'ALERT: interface G0/0 is down!!!'
}
msg_response = requests.post(msg_url,headers=headers,data=json.dumps(msg_body)).json()
