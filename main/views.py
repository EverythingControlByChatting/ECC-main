from django.conf import settings
from django.shortcuts import render, HttpResponse
import json
import requests


def slack_add(request):
    return render(request, 'main/slack/add.html',
                  {'client_id': settings.SLACK_CLIENT_ID})


def slack_oauth(request):
    code = request.GET['code']
    params = {
        'code': code,
        'client_id': settings.SLACK_CLIENT_ID,
        'client_secret': settings.SLACK_CLIENT_SECRET
    }

    url = 'https://slack.com/api/oauth.access'
    json_response = requests.get(url, params)
    data = json.loads(json_response.text)
    print(data)
    if data['access_token'] == settings.SLACK_APP_TOKEN:
        return HttpResponse('Bot added to your Slack team!')
    else:
        return HttpResponse(status=403)
        