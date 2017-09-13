from django.http import JsonResponse

import threading
import requests


class SlashResponse(JsonResponse):
    """
    slash에 대한 응답
    """

    def __init__(self, data=None, response_type="ephemeral",
                 status=200):
        """
        아무 값도 넣지 않을 경우 빈 문자열 200 OK 응답

        :param data: ``dict`` (Json) 또는 ``str``
        :param response_type: "ephemeral" 또는 "in_channel"
        :param status:
        """
        if data is not None \
                and not isinstance(data, dict) \
                and not isinstance(data, str):
            raise TypeError('please use dict(Json) or str type')

        data = "" if data is None else data

        if status != 200 or data == "":
            super(JsonResponse, self).__init__(data, status=status)
        else:
            if isinstance(data, str):
                data = {"response_type": response_type, "text": data}

            super(SlashResponse, self).__init__(data)


class LazySlashResponse(SlashResponse):
    def __init__(self, response_url,
                 func, args=(), kwargs=None, request_result_func=None,
                 waiting_message="_waiting..._", response_type="ephemeral"):
        def async_func(_args, _kwargs):
            result = func(_args, _kwargs)

            json_data = result if isinstance(result, dict) \
                else {"response_type": response_type, "text": result}

            request = requests.post(response_url, json=json_data)

            if request_result_func is not None:
                request_result_func(request)

        super(LazySlashResponse, self).__init__(data=waiting_message)

        threading.Thread(target=async_func, args=args, kwargs=kwargs).start()
