from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from ECC_main.response import slash_response


@csrf_exempt
@require_POST
def wiki_slash_commands(request):
    code = request.POST['text']
    print(code)
    print()
    return slash_response(
        "검색한 단어 : *" + code + "*\n"
        + "> https://ko.wikipedia.org/wiki/" + code
    )
