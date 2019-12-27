#%%
import os
import sys
os.chdir("/home/mamipi/Github/tinpy2/")
sys.path.append(os.path.join(os.path.dirname(__file__), './tinpy'))
#sys.path.append(os.path.join(os.path.dirname('./tinpy'))

import time
import random
import requests
import json
import datetime
import copy
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
''', 'Hello']

#僕も○○好きです、よろしくお願いします
#何のお仕事してるんですか？

def sendMatch(match):
    with requests.Session() as s:
        data = {"id": match.id}
        s.get(url, params=data)

#%%
# 練習用
match_0 = api.getMatch()[0]
if match_0.id=='5a3a6c8b14181c5332add1bb':
    #match_0.name=='Mallory'

#%%
COMMENTOUT='''d
# すべてのマッチに対し、
for match in api.getMatch():
    sendMatch(match)
    messages = match.messages
    # これまでに送ったメッセージが存在しなければ、挨拶を送信
    if len(messages) == 0:
        match.sendMessage("はじめまして{0}さん！\nマッチありがとうございます！".format(match.name))'''

