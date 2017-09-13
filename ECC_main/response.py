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
    """
    Slash에 대한 느린 응답
    """

    def __init__(self, response_url,
                 func, args=(), kwargs=None, request_result_func=None,
                 waiting_message="_waiting..._", response_type="ephemeral"):
        """
        3초 이내에 응답 할 수 없는 경우 사용합니다.

        :param response_url: response_url 값을 넣습니다.
        :param func: 긴 시간의 처리를 하는 함수. `dict`` (Json) 또는 ``str`` 결과를 리턴해야 합니다.
        :param args: ``func``의 args
        :param kwargs: ``func``의 kwargs
        :param request_result_func: 응답의 결과를 받는 함수. 하나의 파라매터를 가지고 있어야 합니다.
        :param waiting_message: 사용자에게 보여지는 waiting message. 빈 문자열은 아무값도 보이지 않습니다.
        :param response_type: "ephemeral" 또는 "in_channel"
        """
        def async_func(*_args, **_kwargs):
            result = func(*_args, **_kwargs)
            if result is not None \
                    and not isinstance(result, dict) \
                    and not isinstance(result, str):
                raise TypeError('please check func return type. dict(Json) or str type')

            json_data = result if isinstance(result, dict) \
                else {"response_type": response_type, "text": result}

            request = requests.post(response_url, json=json_data)

            if request_result_func is not None:
                request_result_func(request)

        super(LazySlashResponse, self).__init__(data=waiting_message)

        threading.Thread(target=async_func, args=args, kwargs=kwargs).start()
