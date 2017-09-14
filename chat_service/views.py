from django.shortcuts import render
from ECC_main.request import slack_slash_request
from ECC_main.response import SlashResponse


@slack_slash_request
def lunch(request):
    text = request.POST['text']
    print('함수')
    return SlashResponse(text)
