import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), './tinpy'))

import time
import random
from tinpy import tinder
from tinpy.accessToken import getAccessToken
from indkeys import *

break_time = 300

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

lat, lon = Sapporo
api.setLocation(lat, lon)

start_time = time.time()
for user in api.getNearbyUsers():
    process_time = time.time() - start_time
    if process_time > break_time:
        break
    user.like()
