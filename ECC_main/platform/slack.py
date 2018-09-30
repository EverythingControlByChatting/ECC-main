from .platformBase import PlatformBase
from django.http import HttpResponse, JsonResponse
from ECC_main.baseRequest import BaseRequest

import ECC_main.settings
import threading
import requests

class Slack(PlatformBase):
    
    def slash_command(request, func):

        token = request.POST['token']
        print(token)
        if ECC_main.settings.SLACK_VERIFICATION_TOKEN == token:
            print("authenticated!")
           
            json_body = Slack._get_json_list(request)
            slash_response = Slack._func_start(json_body, func)
            
            if slash_response.lazy_slash_response is not None:
                Slack.lazy_slash_command(json_body, slash_response)
              
            if slash_response.response_type is None: 
                slash_response['response_type'] = 'ephemeral'
            
            if slash_response.status != 200 or slash_response.text == "":
                json_response = JsonResponse(slash_response, status=slash_response.status)
            else:
                json_response = JsonResponse(slash_response)
            
            return json_response
        else:
            print("unauthenticated")
            return HttpResponse(status=403)
            
    def lazy_slash_command(json_body, slash_response):
        func, args, kwargs, request_result_func = slash_response.lazy_slash_response.get_lazy()
        
        def async_func(*_args, **_kwargs):
            print('lazy send func start')
            slash_response = func(*_args, **_kwargs)
            chat_id = Slack._get_chat_id(json_body)
            response_url = Slack._get_response_url(json_body)
            
            if slash_response.response_type is None: 
                slash_response['response_type'] = 'in_channel'
            
            response = Slack._send_message(slash_response, response_url)
            
            
            if request_result_func is not None:
                request_result_func(response)
            
        threading.Thread(target=async_func, args=args, kwargs=kwargs).start()
   
    def platform():
        return 'slack'
      
    def _get_chat_id(json_body):# return channel_id
        return json_body['channel_id']
        
    def _get_user_id(json_body):
        return json_body['user_id']
        
    def _get_user_name(json_body):
        return json_body['user_name']
        
    def _get_json_list(request_body):
        return request_body.POST
    
    def _get_response_url(json_body):
        return json_body['response_url']
    
    def _func_start(json_body, func):
        platform = Slack.platform()
        text = Slack._get_text(json_body)
        user_name = Slack._get_user_name(json_body)
        user_id = Slack._get_user_id(json_body)
        
        baseRequest = BaseRequest(platform, text, user_name, user_id)
        return func(baseRequest)
        
    def _get_text(json_body):
        return json_body['text']
        
    def _send_message(slash_response, response_url):
        return requests.post(response_url, json=slash_response)