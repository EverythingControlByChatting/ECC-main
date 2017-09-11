from django.shortcuts import HttpResponse
from django.http import JsonResponse


def slash_response(text="", response_type="ephemeral", status=200):
    """
    slash에 대한 응답

    :param text: 빈 문자열일 경우 200 OK 리턴
    :param response_type: "ephemeral" 또는 "in_channel"
    :param status: 200 OK가 아닐경우 해당 status로 설정후 text와 함께 리턴
    :return: JsonResponse 또는 HttpResponse
    """

    if status != 200 or text == "":
        return HttpResponse(text, status=status)
    else:
        return JsonResponse({
            "response_type": response_type,
            "text": text
        })
