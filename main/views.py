from django.shortcuts import render

import settings_secret


def slack_add(request):
    return render(request, 'main/slack/add.html',
                  {'client_id': settings_secret.SLACK_CLIENT_ID})


def slack_oauth(request):
    pass
