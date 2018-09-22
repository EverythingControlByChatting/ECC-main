from django.http import JsonResponse

import threading
import requests

    
class SlashResponse(dict):
    """
    slash에 대한 응답
    """
    
    def __init__(self, data=None):
        """
        :param data: ``dict`` (Json) 또는 ``str``
        """
        super().__init__(self)
        
        self.__status = None
        self.__lazy_slash_response = None
        
        if data is not None \
                and not isinstance(data, dict) \
                and not isinstance(data, str):
            raise TypeError('please use dict(Json) or str type')
            
        if isinstance(data, dict):
            self.update(data)
        else: #str or None
            self['text'] = data
    
    @property
    def text(self):
        return getDict(self, 'text')
    
    @text.setter
    def text(self, new_text):
        self['text'] = new_text
   
    @property 
    def response_type(self): #slack
        return getDict(self, 'response_type')
    
    @response_type.setter
    def response_type(self, new_response_type):
        """
        
        :param response_type: "ephemeral" 또는 "in_channel"
        """
        self['response_type'] = new_response_type
        
    @property
    def status(self):
        return self.__status 
    @status.setter
    def status(self, new_status):
        self.__status = new_status
    
    @property
    def lazy_slash_response(self):
        return self.__lazy_slash_response
    
    @lazy_slash_response.setter
    def lazy_slash_response(self, lazySlashResponse):
        self.__lazy_slash_response = lazySlashResponse
        

class LazySlashResponse:
    """
    slash에 대한 느린 응답에 대한 함수를 설정 가집니다.
    3초 이내에 응답할 수 없는 경우 사용합니다.(slack 기준)
    
    :param func: 긴 시간의 처리를 하는 함수. ``dict`` (Json) 또는 ``str`` 결과를 리턴해야 합니다.
    :param args: ``func``의 args
    :param kwargs: ``func``의 kwargs
    :param request_result_func: 응답의 결과를 받는 함수. 하나의 파라매터를 가지고 있어야 합니다.
    """
    
    def __init__(self, func, args=(), kwargs=None, request_result_func=None):
        self.func = func
        self.func_args = args
        self.func_kwargs = kwargs
        self.request_result_func = request_result_func
        
    def get_lazy(self):
        return self.func, self.func_args, self.func_kwargs, self.request_result_func

def getDict(dic, key):
    if (key in dic):
        return dic[key]
    else:
        return None
