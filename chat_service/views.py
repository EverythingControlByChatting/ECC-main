from django.shortcuts import render
from ECC_main.request import slack_slash_request
from ECC_main.response import SlashResponse
from . import crowling
import json

@slack_slash_request
def lunch(request):
    text = request.POST['text']
    respon= crowling.crowlier_lunch(text)
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

@slack_slash_request
def lunch_category(request):
    text = request.POST['text']
    respon= crowling.lunch_category()
    
    list1 = []

    for first in respon:
        list1.append({
        'title': first,
        'short': True
    })
    return SlashResponse({
    "attachments": [
        {
            "title": "맛집 카테고리입니다",
            "fields": list1,
            "color": "#F35A00",
        }
    ]
})