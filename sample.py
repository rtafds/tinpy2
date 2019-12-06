import tinpy
from tinpy import getAccessToken

FBemail = ""
FBpass = ""

token = getAccessToken(FBemail, FBpass)
api = tinpy.API(token)

# This is the latitude and the longitude of Shibuya Tokyo Japan.
lat, lon = 35.658034, 139.701636

api.setLocation(lat, lon)

for user in api.getNearbyUsers():
    user.like()
