from abc import ABCMeta, abstractmethod

class PlatformBase(metaclass=ABCMeta):
    @abstractmethod
    def slash_command(request, func):
        pass
    
    @abstractmethod
    def lazy_slash_command(request, func):
        pass
   
    @abstractmethod
    def platform():
        pass
      
    @abstractmethod
    def _get_chat_id(json_body):
        pass
        
    @abstractmethod
    def _get_user_id(json_body):
        pass
        
    @abstractmethod
    def _get_user_name(json_body):
        pass
        
    @abstractmethod
    def _get_json_list(request_body):
        pass