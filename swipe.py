#%%
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), './tinpy'))

import time
import random
import requests
import json
import datetime
import copy
from tinpy import tinder
from tinpy.accessToken import getAccessToken
from indkeys import *

#%%
break_time = 300
nope_rate = 0.0

def sendProfile(user):
    data = {"id": user.id, "name": user.name,
            "age": user.age, "gender": user.gender}
    data["bio"] = user.bio
    for i in range(len(user.photos)):
        data["photo{0}".format(i)] = user.photos[i]
    data["videos"] = user.videos
    data["schools"] = user.schools
    data["jobs"] = user.jobs
    data["distance_mi"] = user.distance_mi
    with requests.Session() as s:
        s.post(url, data=data)

token = getAccessToken(FBemail, FBpass)
api = tinder.API(token)

# This is the latitude and the longitude of Shibuya Tokyo Japan.

Nagoya = (35.181451, 136.906557)
Shibuya = (35.658034, 139.701636)
Sapporo = (43.061771, 141.354451)
Sendai = (38.268195, 140.869418)
Osaka = (34.693725, 135.502254)
Fukuoka = (33.590184, 130.401689)
Okinawa = (26.120191, 127.702501)

lat, lon = Nagoya
api.setLocation(lat, lon)

start_time = time.time()
for user in api.getNearbyUsers():
    process_time = time.time() - start_time
    if process_time > break_time:
        break

    if api.getLikesRemaining() == 0:
        break

    if random.random() < nope_rate:
        user.nope()
    else:
        user.like()
    sendProfile(user)
