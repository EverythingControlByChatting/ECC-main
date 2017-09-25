from ECC_main.request import slack_slash_request
from ECC_main.response import SlashResponse
import settings_secret
import requests as r

HOST = settings_secret.HOST
PORT = settings_secret.PORT

@slack_slash_request
def on(request):
    print("1")
    try:
        text = request.POST['text'].split()[0]
    except:
        text = '22'
    print(HOST+":"+PORT+'/on'+text)
    cons = r.get(HOST+":"+PORT+'/on'+text)
    print(cons)
    if cons.status_code == 200:
        return SlashResponse("ok " + text)
    else:
        return SlashResponse("deny on " + text)

@slack_slash_request
def off(request):
    cons = r.get(HOST + ":" + PORT + '/off')
    if cons.status_code == 200:
        return SlashResponse("ok")
    else:
        return SlashResponse("deny off")

@slack_slash_request
def super(request):
    cons = r.get(HOST + ":" + PORT + '/super')
    if cons.status_code == 200:
        return SlashResponse("ok")
    else:
        return SlashResponse("deny super")

@slack_slash_request
def set(request):
    try:
        text = request.POST['text'].split()[0]
    except:
        text = '22'
    cons = r.get(HOST+":"+PORT+'/set'+text)
    if cons.status_code == 200:
        return SlashResponse("ok " + text)
    else:
        return SlashResponse("deny set " + text)