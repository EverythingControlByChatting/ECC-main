import re
import time

from ECC_main.request import slack_slash_request
from ECC_main.response import SlashResponse, LazySlashResponse


@slack_slash_request
def wiki_slash_commands(request):
    code = request.POST['text']
    print(code)
    print()
    return SlashResponse(
        "검색한 단어 : *" + code + "*\n"
        + "> https://ko.wikipedia.org/wiki/" + code
    )


@slack_slash_request
def short_delay_message(request):
    COMMAND_REGEX = '(?P<second>\d+([.]\d)?)[,]\s?(?P<message>.+)'

    p = re.compile(COMMAND_REGEX, re.DOTALL)

    text = request.POST['text']
    response_url = request.POST['response_url']
    user_id = request.POST['user_id']
    user_name = request.POST['user_name']

    print(text)

    if p.match(text) is None:
        return SlashResponse("유효하지 않은 명령입니다.")

    m = p.search(text)

    delay_time = float(m.group("second"))
    message = m.group("message")

    if delay_time > 60 * 30:
        return SlashResponse("유효하지 않은 시간입니다.\n30분 이내로 설정해 주십시오")

    def delay_message():
        time.sleep(delay_time)
        return "_<@" + user_id + "|" + user_name + ">님이 예약한 메시지_\n\n" + message

    waiting_message = "*" + str(delay_time) + "* 초 뒤에\n```" + \
                      message + "```\n가 전달됩니다."

    return LazySlashResponse(
        response_url, delay_message,
        request_result_func=showRequest,
        waiting_message=waiting_message,
        response_type="in_channel"
    )


def showRequest(request):
    print(request)
