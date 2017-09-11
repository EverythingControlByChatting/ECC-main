from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


@csrf_exempt
@require_POST
def wiki_slash_commands(request):
    code = request.POST['text']
    print(code)
    print()
    return JsonResponse({
        "text": "검색한 단어 : *" + code + "*\n"
                + "> https://ko.wikipedia.org/wiki/" + code
    })
