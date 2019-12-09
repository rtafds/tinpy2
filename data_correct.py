import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), './tinpy'))

from tinpy import tinder
from tinpy.accessToken import getAccessToken
from indkeys import *
import requests
import json


url = "https://script.google.com/macros/s/AKfycbyFKJsT0MRGG_A3h_E16vAX6Zc45zvFkbx7xd6RXZqBi8owi-n9/exec"
token = tinpy.getAccessToken(FBemail, FBpass)
#token = "Facebookのアクセストークン"


api = tinder.API(token)

api.setLocation(35.658034, 139.701636)


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


def sendMatch(match):
    with requests.Session() as s:
        data = {"id": match.id}
        s.get(url, params=data)


for user in api.getNearbyUsers():
    if api.getLikesRemaining() == 0:
        break
    user.like()
    sendProfile(user)

for match in api.getMatch():
    sendMatch(match)
    messages = match.messages
    if len(messages) == 0:
        match.sendMessage(
            "はじめまして{0}さん！ マッチありがとうございます！".format(match.name))

