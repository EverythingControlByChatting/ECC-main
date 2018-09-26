import re
import time

from ECC_main.request import slack_slash_request, slash_request
from ECC_main.response import SlashResponse, LazySlashResponse
from ECC_main.platform.telegram import Telegram


@slash_request
def wiki_slash_commands(request):
    code = request['text']
    print(code)
    print()
    return SlashResponse("검색한 단어 : *" + code + "*\n"
        + "> https://ko.wikipedia.org/wiki/" + code)


@slash_request
def short_delay_message(request):
    COMMAND_REGEX = '(?P<second>\d+([.]\d)?)[,]\s?(?P<message>.+)'

    p = re.compile(COMMAND_REGEX, re.DOTALL)
   
    platform = request['platform'] 
    text = request['text']
    user_id = request['user_id']
    user_name = request['user_name']
    print('text ', text)
    
    if p.match(text) is None:
        return SlashResponse("유효하지 않은 명령입니다.")
    
    m = p.search(text)
    
    delay_time = float(m.group("second"))
    message = m.group("message")
    
    if delay_time > 60 * 30:
        return SlashResponse("유효하지 않은 시간입니다.\n30분 이내로 설정해 주십시오")
        
    def delay_message():
        time.sleep(delay_time)
        send_message = user_name + ">님이 예약한 메시지_\n\n" + message
        
        if platform is Telegram.platform():
            send_message = "_<" + send_message
        else:
            send_message = "_<@" + user_id + "|" + send_message
        
        return SlashResponse(send_message)

    waiting_message = "*" + str(delay_time) + "* 초 뒤에\n```" + \
                      message + "```\n가 전달됩니다."
                     
    slash_response = SlashResponse(waiting_message)
    slash_response.lazy_slash_response = LazySlashResponse(
        delay_message, 
        request_result_func=showRequest
    )
    
    return slash_response


def showRequest(request):
    print('lazy request: ', request)
    print('lazy request: ', request.content)