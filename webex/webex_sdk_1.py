from webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI(
    access_token='NDAxZGRlNGMtMWVmZC00ZDhjLThkMTUtMjUyNTFkYmVhZWZlNTAyYWY5MGEtM2Ni_P0A1_4324cf20-3dc3-4497-af07-1b996464c625'
)

all_rooms = api.rooms.list()
demo_rooms = [room for room in all_rooms if 'oldest Demo' om room.title]

for room in demo_rooms:
    api.rooms.__delete__(room.id)

demo_room = api.rooms.__create__('newtest demo')
email_address = ['user1@test.com','user2@test.com']
for email in email_address:
    api.memberships.create(demo_room.id,personEmail=email)
api.message.create(demo_room.id,text='prueba!!!!')
