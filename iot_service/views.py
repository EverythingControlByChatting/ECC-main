from ECC_main.request import slack_slash_request
from ECC_main.response import SlashResponse
import requests as r

HOST = ## raspberry pi ##
PORT = ## port number ##

@slack_slash_request
def on(request):
    try:
        text = request.POST['text'].split()[0]
    except:
        text = '22'
    cons = r.get(HOST+":"+PORT+'/on'+text)
    if cons.status_code == '200':
        return SlashResponse("ok " + text)
    else:
        return SlashResponse("deny on " + text)

@slack_slash_request
def off(request):
    cons = r.get(HOST + ":" + PORT + '/off')
    if cons.status_code == '200':
        return SlashResponse("ok")
    else:
        return SlashResponse("deny off")

@slack_slash_request
def super(request):
    cons = r.get(HOST + ":" + PORT + '/super')
    if cons.status_code == '200':
        return SlashResponse("ok")
    else:
        return SlashResponse("deny super")

@slack_slash_request
def cold(request):
    try:
        text = request.POST['text'].split()[0]
    except:
        text = '22'
    cons = r.get(HOST+":"+PORT+'/cold'+text)
    if cons.status_code == '200':
        return SlashResponse("ok " + text)
    else:
        return SlashResponse("deny cold " + text)