#%%
import os
import sys
os.chdir("/home/mamipi/Github/tinpy2/")
sys.path.append(os.path.join(os.path.dirname(__file__), './tinpy'))

import requests
import json
import time
import random
from accessToken import getAccessToken
from tinpy import tinder
from indkeys import *


# アクセストークンを取得
token = getAccessToken(FBemail, FBpass)

# APIクラスを呼び出し
api = tinder.API(token)

message_list = ['もしかして天使？','ギョギョギョッ！サカナ食べに行こ！',
 '1+1の本当の答え知りたくない？','タイプです','こんにちわんこそば', 'はじめましてよかったら仲良くしてください',
'''
もうね。
会う前から好き。
なにそのつぶらな瞳。
まつげ。
もう何度でも言うけど
#会う前から好き
''', 'aaa']

#僕も○○好きです、よろしくお願いします
#何のお仕事してるんですか？

def sendMatch(match):
    with requests.Session() as s:
        data = {"id": match.id}
        s.get(url, params=data)


# すべてのマッチに対し、
for match in api.getMatch():
    sendMatch(match)
    messages = match.messages
    # これまでに送ったメッセージが存在しなければ、挨拶を送信
    if len(messages) == 0:
        match.sendMessage("はじめまして{0}さん！\nマッチありがとうございます！".format(match.name))

