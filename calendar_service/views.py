from django.shortcuts import render, HttpResponse
from ECC_main.request import slack_slash_request
from ECC_main.response import SlashResponse, LazySlashResponse
from . import gcalendar
from oauth2client import client
import settings_secret
import httplib2, os, codecs
from apiclient.discovery import build

tf = {False:'실패 하였습니다',True:'성공 하였습니다',}
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'calendar_service/client_secret.json'
PROJECT_NAME = 'Google Calendar'

def get_credential(request):
    user_id = request.POST['user_id']
    google_calendar = gcalendar.GCalendar(user_id)
    return google_calendar

@slack_slash_request
def calendarlist(request):
    google_calendar = get_credential(request)
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
    google_calendar = get_credential(request)
    data = [l.strip() for l in request.POST['text'].split(',') if l.strip()]

    if len(data) != 4:
        b = False
    else:
        b = google_calendar.insert_Calendar(summary=data[0], body=data[1], start=data[2], end=data[3])
    
    if type(b) == bool:
        result = SlashResponse({
            'attachments': [
                {
                    'pretext': '이벤트 추가',
                    'text':data[1]+' 이벤트 추가에 '+tf[b],
                    'color': '#7CD197',
                }
            ]
        })
    else:
        result = SlashResponse({
            'attachments': [
                {
                    'pretext': '이벤트 추가',
                    'text':b,
                    'color': '#7CD197',
                }
            ]
        })
    return result

@slack_slash_request
def eventdelete(request):
    google_calendar = get_credential(request)
    data = [l.strip() for l in request.POST['text'].split(',') if l.strip()]
    
    if len(data) != 2:
        b = False
    else:
        b = google_calendar.delete_Calendar(summary=data[0],event_summary=data[1])

    if type(b) == bool:
        result = SlashResponse({
            'attachments': [
                {
                    'pretext': '이벤트 삭제',
                    'text':data[1]+' 이벤트 삭제에 '+tf[b],
                    'color': '#7CD197',
                }
            ]
        })
    else:
        result = SlashResponse({
            'attachments': [
                {
                    'pretext': '이벤트 삭제',
                    'text':b,
                    'color': '#7CD197',
                }
            ]
        })
    return result

@slack_slash_request
def eventupdate(request):
    google_calendar = get_credential(request)
    data = [l.strip() for l in request.POST['text'].split(',') if l.strip()]
    
    if len(data) == 3:
        b = google_calendar.update_Calendar(summary=data[0],event_summary=data[1],update_summary=data[2])
    elif len(data) == 5:
        b = google_calendar.update_Calendar(summary=data[0],event_summary=data[1],update_summary=data[2], sndate=[data[3],data[4]])
    else:
        b = False
    
    if type(b) == bool:
        result = SlashResponse({
            'attachments': [
                {
                    'pretext': '이벤트 수정',
                    'text':data[1]+' 에서 '+data[2]+'로'+' 이벤트 수정에 '+tf[b],
                    'color': '#7CD197',
                }
            ]
        })
    else:
        result = SlashResponse({
            'attachments': [
                {
                    'pretext': '이벤트 수정',
                    'text':b,
                    'color': '#7CD197',
                }
            ]
        })
    return result

@slack_slash_request
def eventlist(request):
    google_calendar = get_credential(request)
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
    google_calendar = get_credential(request)
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

def redirect(request):
    auth_code = request.GET['code']
    user_id = request.GET['state']
    flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, scope=SCOPES, redirect_uri=settings_secret.REDIRECT_URI)
    flow.user_agent = PROJECT_NAME
    flow.params['access_type'] = 'offline'
    auth_uri = flow.step1_get_authorize_url()
    credentials = flow.step2_exchange(auth_code)
    http_auth = credentials.authorize(httplib2.Http())
    google_calendar = build('calendar', 'v3', http=http_auth)
    
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    credential_path = os.path.join(credential_dir, user_id+'.json')
    with codecs.open(credential_path, 'w', 'utf-8') as f:
        f.write(credentials.to_json())

    return HttpResponse(str("Google Calendar Login Success"))