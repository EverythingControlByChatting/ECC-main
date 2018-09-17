from django.conf import settings
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from calendar_service.telegram_utils import send_message
import settings_secret

import request
import json
import requests

TOKEN = settings_secret.TELEAGRAM_TOKEN
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

# # Create your views here.

#  https://api.telegram.org/bot633554677:AAHleVKSQ2GC4wLhVQk4mwT9tCizhCsW2XU/setWebhook?url=https://telegram-bot-kokihoon.c9users.io/set_webhook/set_webhook
@csrf_exempt
def set_webhook(requests):
    json_list = json.loads(requests.body)
    chat_id = json_list['message']['chat']['id']
    command = json_list['message']['text']
    send_message(command, chat_id)
    return HttpResponse()