from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import resolve, get_resolver
from ECC_main.platform.telegram import Telegram 

import json

@csrf_exempt
def webhook(request):
    print('get telegram message!!')
    telegram_body = request.body
    json_list = json.loads(telegram_body)
    json_list['chat_platform_type'] = 'telegram'
    request.POST = json_list
   
    slash_command = None
    print(json_list)
    slash_command, _ = Telegram.cutCommand(json_list)

    print('slected slash command ', slash_command)
    if slash_command is None:
        print('invalid data from telegram: ', telegram_body)
        return HttpResponse()
        
    # TODO 예외처리
    print('slash command :', slash_command)
    urls = get_resolver(None).reverse_dict
    if slash_command not in urls:
        print('invalid command from telegram: ', slash_command)
        return HttpResponse()
        
    path = '/' + urls[slash_command][1].replace('\\', '')[:-1]
    print(path) 
    func, _, _ = resolve(path)
    
    return func(request)
