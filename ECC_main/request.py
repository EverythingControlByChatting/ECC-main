from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .platform.telegram import Telegram
from .platform.slack import Slack

import ECC_main.settings
import json


def slack_slash_request(func):
    @csrf_exempt
    @require_POST
    def decorator(*args, **kwargs):
        request = args[0]
        token = request.POST['token']

        if ECC_main.settings.SLACK_VERIFICATION_TOKEN == token:
            print("authenticated!")
            result = func(*args, **kwargs)
            return result
        else:
            print("unauthenticated")
            return HttpResponse(status=403)

    return decorator
   
    
def slash_request(func):
    @csrf_exempt
    @require_POST
    def decorator(*args, **kwargs):
        request = args[0]
        chat_platform_type = None
        
        if 'chat_platform_type' in request.POST:
            chat_platform_type = request.POST['chat_platform_type']
        
        if chat_platform_type is 'telegram':
            result = Telegram.slash_command(request, func)
        else: # Slack
            result = Slack.slash_command(request, func)
            
        return result

    return decorator
