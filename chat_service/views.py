from django.shortcuts import render
from ECC_main.request import slack_slash_request
from ECC_main.response import SlashResponse
from . import Crowling
import json

@slack_slash_request
def lunch(request):
    text = request.POST['text']
    respon= crowling1.crowlier(text)
    respon1 = list(zip(respon[0], respon[1]))
    list1 = []

    for (first, last) in respon1:
        list1.append({
        'title': first,
        'value': last,
        'short': True
    })

    return SlashResponse({
    "attachments": [
        {
            "title": text+" 맛집입니다.",
            "fields":list1,
            "color": "#F35A00",
        }
    ]
})