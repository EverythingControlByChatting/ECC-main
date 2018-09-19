from .platformBase import PlatformBase
from django.http import HttpResponse
from ECC_main.baseRequest import BaseRequest

import threading
import json
import requests
import settings_secret

URL = "https://api.telegram.org/bot{0}/sendMessage".format(settings_secret.TELEGRAM_TOKEN)

class Telegram(PlatformBase):
    
    def slash_command(request, func):
        json_list = Telegram._get_json_list(request.body)
        slash_response = Telegram._func_start(json_list, func)
        
        chat_id = Telegram._get_chat_id(json_list)
        Telegram._send_message(slash_response, chat_id)
        
        if slash_response.lazy_slash_response is not None:
            Telegram.lazy_slash_command(json_list, slash_response)
        
        return HttpResponse()
        
        
    def lazy_slash_command(json_list, slash_response):
        func, args, kwargs, request_result_func = slash_response.lazy_slash_response.get_lazy()
        
        def async_func(*_args, **_kwargs):
            print('lazy send func start')
            slash_response = func(*_args, **_kwargs)
            chat_id = Telegram._get_chat_id(json_list)
            response = Telegram._send_message(slash_response, chat_id)
            
            if request_result_func is not None:
                request_result_func(response)
            
        threading.Thread(target=async_func, args=args, kwargs=kwargs).start()
    
    def platfrom():
        return 'telegram'
      
    def _get_chat_id(json_body):
        return str(json_body['message']['chat']['id'])
        
    def _get_user_id(json_body):
        return str(json_body['message']['from']['id'])
        
    def _get_user_name(json_body):
        return json_body['message']['from']['username']
        
    def _get_json_list(request_body):
        return json.loads(request_body)
    
    def _func_start(json_list, func):
        platfrom = Telegram.platfrom()
        _, text = Telegram.cutCommand(json_list)
        user_name = Telegram._get_user_name(json_list)
        user_id = Telegram._get_user_id(json_list)
        
        return func(BaseRequest(platfrom, text, user_name, user_id))
        
    
    def _send_message(data, chat_id, parse_mode="MARKDOWN"):
        data.update({'chat_id': chat_id, 'parse_mode': parse_mode})
        
        return requests.post(URL, json=data)
        
        
    def cutCommand(json_list):
        if "message" in json_list:
            if "entities" in json_list["message"]:
                for entity in json_list["message"]["entities"]:
                    if "bot_command" in entity["type"]:
                        length = entity["length"]
                        text = json_list["message"]["text"]
                        slash_command = text[1:length].replace('_','-')
                        length = length + 1
                        data = text[length:]
                        
                        return slash_command, data
                        
        return None, None
        