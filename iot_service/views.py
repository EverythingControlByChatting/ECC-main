from ECC_main.request import slack_slash_request
from ECC_main.response import SlashResponse
import settings_secret
import requests

HOST = settings_secret.HOST
PORT = settings_secret.PORT


@slack_slash_request
def acon(request):
    """
    Turn on the Air Conditioner
    :param
        request: ## SERVER ## /on [Temperature]

    :return:
        success (response_type="in_channel")
            Turn on the Air Conditioner [Temperature]

        failed (response_type="ephemeral")
            Failed Command
    """
    try:
        text = request.POST['text'].split()[0]
    except IndexError:
        text = '22'
    print(HOST + ":" + PORT + '/on' + text)
    cons = requests.get(HOST + ":" + PORT + '/on' + text)
    print(cons)
    if cons.status_code == 200:
        return SlashResponse("에어컨이 켜집니다. " + text + "°C", response_type="in_channel")
    else:
        return SlashResponse("Failed Connection with iot Server")


@slack_slash_request
def acoff(request):
    """
    Turn Off the Air Conditioner
    :param
        request: ## SERVER ## /off
    :return:
        success (response_type="in_channel")
            Turn Off the Air Conditioner
        failed (response_type="ephemeral")
            Failed Connection with iot Server
    """
    cons = requests.get(HOST + ":" + PORT + '/off')
    if cons.status_code == 200:
        return SlashResponse("에어컨이 꺼집니다.", response_type="in_channel")
    else:
        return SlashResponse("Failed Connection with iot Server")


@slack_slash_request
def acsuper(request):
    """
    Power Cooling Mode
    :param
        request: ## SERVER ## /acsuper
    :return:
        success (response_type="in_channel")
            Turn Off the Air Conditioner
        failed (response_type="ephemeral")
            Failed Connection with iot Server
    """
    cons = requests.get(HOST + ":" + PORT + '/super')
    if cons.status_code == 200:
        return SlashResponse("파워냉방 설정", response_type="in_channel")
    else:
        return SlashResponse("Failed Connection with iot Server")


@slack_slash_request
def achelp(request):
    text = "[에어컨 명령어]\n" \
           "acon | acoff | acsuper | achelp\n\n" \
           "acon[온도]\n: 에어컨을 켭니다\n" \
           ": 에어컨을 [온도]로 설정합니다.\n"\
           "acoff\n: 에어컨을 끕니다.\n"\
           "acsuper\n: 파워냉방 모드로 설정합니다.\n"
    return SlashResponse(text)