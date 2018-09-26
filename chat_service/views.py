from django.shortcuts import render
from ECC_main.request import slack_slash_request, slash_request
from ECC_main.response import SlashResponse
from ECC_main.platform.telegram import Telegram 
from . import crowling
import json


@slash_request
def lunch(request):
    text = request['text']
    respon= crowling.crowlier_lunch(text)
    respon1 = list(zip(respon[0], respon[1]))
    list1 = []

    if request['platform'] is Telegram.platform():
        for (first, last) in respon1:
            list1.append(first)
            list1.append("주소 : " + last)
            
        test = str(list1)
        count = 0
        number = 0 
        list_str = []
        
        for mark in test:
            if test[number] == ',':
                count = count + 1
            if count == 3:
                if test[number] == ',':
                    list_str.append('\n')
            if count == 4:
                if test[number] == ',':
                    list_str.append('\n')
                    count = 0
            else:    
                list_str.append(test[number])
            number = number + 1
        
        test = "".join(list_str)
        test = str(test)
        
        result = "*맛집 결과?*\n\n"
        result = result + test
        slashResponse = SlashResponse(
            result
        )
        
    else:
        
      for (first, last) in respon1:
        list1.append({
        'title': first,
        'value': last,
        'short': True
      })        
        
      slashResponse = SlashResponse({
        "attachments": [
            {
                "title": text+" 맛집입니다.",
                "fields":list1,
                "color": "#F35A00",
            }
        ]
    })
    return slashResponse;

@slash_request
def lunch_category(request):
    text = request['text']
    respon= crowling.lunch_category()
    
    list1 = []
        
    if request['platform'] is Telegram.platform():
        for first in respon:
            if first != '전체보기':
                list1.append(" "+ first + " ")
            
        test = str(list1)
        count = 0
        number = 0 
        list_str = []
        
        for mark in test:
            if test[number] == ',':
                list_str.append('\n')
            else:    
                list_str.append(test[number])
            number = number + 1
        
        test = "".join(list_str)
        test = str(test)    
        
        result = "*맛집 카테고리*\n\n"
        result = result + test
        print(result)
        slashResponse = SlashResponse(
            result
        )
        return slashResponse
    else:
        
        for first in respon:
            list1.append({
            'title': first,
            'short': True
        })
        return SlashResponse({
        "attachments": [
            {
                "title": "맛집 카테고리입니다",
                "fields": list1,
                "color": "#F35A00",
            }
        ]
    })