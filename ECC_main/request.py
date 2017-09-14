from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

import ECC_main.settings


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
