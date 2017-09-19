from django.shortcuts import render
from ECC_main.request import slack_slash_request
from ECC_main.response import SlashResponse, LazySlashResponse
from . import gcalendar

tf = {False:'실패 하였습니다',True:'성공 하였습니다',}
google_calendar = gcalendar.GCalendar()

@slack_slash_request
def calendarlist(request):
    calendarList = '\r\n'.join(google_calendar.get_Calendar())
        
    return SlashResponse({
        'attachments': [
            {
                'pretext': '캘린더 리스트',
                'text':calendarList,
                'color': '#7CD197',
            }
        ]
    })

@slack_slash_request
def eventinsert(request):
    data = [l.strip() for l in request.POST['text'].split(',') if l.strip()]

    if len(data) != 4:
        b = False
    else:
        b = google_calendar.insert_Calendar(summary=data[0], body=data[1], start=data[2], end=data[3])
    
    result = SlashResponse({
        'attachments': [
            {
                'pretext': '이벤트 추가',
                'text':data[1]+' 이벤트 추가에 '+tf[b],
                'color': '#7CD197',
            }
        ]
    })
    return result

@slack_slash_request
def eventdelete(request):
    data = [l.strip() for l in request.POST['text'].split(',') if l.strip()]
    
    if len(data) != 2:
        b = False
    else:
        b = google_calendar.delete_Calendar(summary=data[0],event_summary=data[1])

    result = SlashResponse({
        'attachments': [
            {
                'pretext': '이벤트 삭제',
                'text':data[1]+' 이벤트 삭제에 '+tf[b],
                'color': '#7CD197',
            }
        ]
    })
    return result

@slack_slash_request
def eventupdate(request):
    data = [l.strip() for l in request.POST['text'].split(',') if l.strip()]
    
    if len(data) == 3:
        b = google_calendar.update_Calendar(summary=data[0],event_summary=data[1],update_summary=data[2])
    elif len(data) == 5:
        b = google_calendar.update_Calendar(summary=data[0],event_summary=data[1],update_summary=data[2], sndate=[data[3],data[4]])
    else:
        b = False
    
    result = SlashResponse({
        'attachments': [
            {
                'pretext': '이벤트 수정',
                'text':data[1]+' 에서 '+data[2]+'로'+' 이벤트 수정에 '+tf[b],
                'color': '#7CD197',
            }
        ]
    })
    return result

@slack_slash_request
def eventlist(request):
    data = [l.strip() for l in request.POST['text'].split(',') if l.strip()]

    if len(data) != 2:
        b = []
    else:
        b = google_calendar.list_Calendar(summary=data[0], maxResult=int(data[1]))
    
    b = '\r\n'.join(b).strip()
    if not b.strip():
        b = '출력할 데이터가 없습니다'

    result = SlashResponse({
        'attachments': [
            {
                'pretext': '이벤트 리스트',
                'text':b,
                'color': '#7CD197',
            }
        ]
    })
    return result

@slack_slash_request
def help(request):
    text = google_calendar.help()

    return SlashResponse({
        'attachments': [
            {
                'pretext': '도움말',
                'text':text,
                'color': '#7CD197',
            }
        ]
    })