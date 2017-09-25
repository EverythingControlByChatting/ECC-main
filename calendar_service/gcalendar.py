import httplib2, os, re, datetime
from googleapiclient import discovery
from calendar_service.oauth_credentials import oauth_credentials

p = {True:re.compile(r'(\d+)[\.](\d+)[\.](\d+)[-](\d+)[:](\d+)'), False:re.compile(r'(\d+)[\.](\d+)[\.](\d+)')}
range_number = {True:6, False:4}
time_format = {
    True:'{d[0]}-{d[1]}-{d[2]}T{d[3]}:{d[4]}:00+09:00',
    False:'{d[0]}-{d[1]}-{d[2]}'
}

@oauth_credentials
def get_credentials(credentials):
    return credentials

def get_Events(calendarInfo, service, maxResult=None):
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 현재 시간
    calendarId = calendarInfo[0].get('id')
    eventResult = service.events().list(
        calendarId=calendarId,
        timeMin=now,
        maxResults=maxResult,
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    events = eventResult.get('items', [])
    return events

class GCalendar:
    def __init__(self, user_id):
        self.credentials = get_credentials(user_id)
        """
        여기서 확인 필요.
        """
        if self.credentials.__class__ !=  str:
            http = self.credentials.authorize(httplib2.Http())
            self.service = discovery.build('calendar', 'v3', http=http)
            self.calL = self.service.calendarList().list().execute()['items']
        else:
            self.service = None
            self.calL = None
    
    def get_Calendar(self):
        if self.service != None:
            calNL = [l.get('summary') for l in self.calL]
            return calNL
        else:
            return [self.credentials]

    def insert_Calendar(self, summary='', body=None, start=None, end=None):
        if self.service != None:
            calendarInfo = [l for l in self.calL if l.get('summary') == summary]
            if len(calendarInfo) != 1:
                print('실패하였습니다'); return False
            else:
                try:
                    dateTime = (lambda x: '-' in x)(start)
                    dateTF = {True:"dateTime", False:"date"}

                    m = p[dateTime].search(start)
                    start_data = [m.group(i) for i in range(1, range_number[dateTime])]
                    m = p[dateTime].search(end)
                    end_data = [m.group(i) for i in range(1, range_number[dateTime])]

                    start = time_format[dateTime].format(d=start_data)
                    end = time_format[dateTime].format(d=end_data)

                    calendarId = calendarInfo[0].get('id')
                    body = {
                        "start": {dateTF[dateTime]: start},
                        "end": {dateTF[dateTime]: end},
                        "summary": body
                    }
                    self.service.events().insert(
                        calendarId=calendarId,
                        body=body
                    ).execute()

                    print('캘린더 추가에 성공하였습니다.')
                    return True
                except Exception as e:
                    print(e)
                    print('실패하였습니다'); return False
        else:
            return self.credentials

    def list_Calendar(self, summary='', maxResult=10):
        if self.service != None:
            calendarInfo = [l for l in self.calL if l.get('summary') == summary]

            if len(calendarInfo) != 1:
                print('이벤트 검색에 실패하였습니다.'); return False
            else:
                try:
                    events = get_Events(calendarInfo, self.service, maxResult)
                    eventList = []
                    for event in events:
                        if 'date' in event.get('start', []):
                            eventList.append(event['start']['date']+' ~ '+event['end']['date']+'\t'+event['summary'])
                        else:
                            eventList.append(event['start']['dateTime'] + '~' + event['end']['dateTime'] +'\t'+event['summary'])
                    return eventList
                except Exception as e:
                    print(e)
                    print('이벤트 검색에 실패하였습니다.'); return False
        else:
            return [self.credentials]

    def delete_Calendar(self, summary='', event_summary=''):
        if self.service != None:
            event_Id=''
            calendarInfo = [l for l in self.calL if l.get('summary') == summary]

            if len(calendarInfo) != 1:
                print('이벤트 검색에 실패하였습니다.'); return False
            else:
                try:
                    events = get_Events(calendarInfo, self.service)
                    
                    for event in events:
                        if event.get('summary') == event_summary:
                            event_Id=event.get('id')
                            break

                    self.service.events().delete(
                        calendarId=calendarInfo[0].get('id'),
                        eventId=event_Id
                    ).execute()

                    print('삭제에 성공하였습니다.')
                    return True
                except Exception as e:
                    print('이벤트 삭제에 실패하였습니다.'); return False
        else:
            return self.credentials

    def update_Calendar(self, summary='', event_summary='', update_summary='', sndate=['','']):
        if self.service != None:
            event_Id=''
            calendarInfo = [l for l in self.calL if l.get('summary') == summary]

            if len(calendarInfo) != 1:
                print('이벤트 검색에 실패하였습니다.'); return False
            else:
                try:
                    events = get_Events(calendarInfo, self.service)

                    for event in events:
                        if event.get('summary') == event_summary:
                            event_Id=event.get('id')
                            if sndate==['','']:
                                if 'date' in event.get('start', []):
                                    sndate[0]=event.get('start').get('date')
                                    sndate[1]=event.get('end').get('date')
                                else:
                                    sndate[0]=event.get('start').get('dateTime')
                                    sndate[1]=event.get('end').get('dateTime')
                            break
                    
                    dateTime = (lambda x: 'T' in x)(sndate[0])
                    dateTF = {True:"dateTime", False:"date"}
                    body = {
                        "start": {dateTF[dateTime]: sndate[0]},
                        "end": {dateTF[dateTime]: sndate[1]},
                        "summary": update_summary
                    }
                    self.service.events().update(
                        calendarId=calendarInfo[0].get('id'),
                        eventId=event_Id,
                        body=body
                    ).execute()

                    print('이벤트 수정에 성공하였습니다.')
                    return True
                except Exception as e:
                    print(e)
                    print('이벤트 수정에 실패하였습니다.'); return False
        return self.credentials

    def help(self):
        text = "To print a Calendar list\r\n" + \
               "=> /calendarlist\r\n\r\n" + \
               "To add an event\r\n" + \
               "=> /eventinsert summary, body, startTime(YYYY.MM.DD-hh:mm or YYYY.MM.DD), endTime(YYYY.MM.DD-hh:mm or YYYY.MM.DD)\r\n\r\n" + \
               "To delete an event\r\n" + \
               "=> /eventdelete summary, event_summary\r\n\r\n" + \
               "To update an event(startTime and endTime can be omitted)\r\n" + \
               "=> /eventupdate summary, event_summary, update_summary, startTime, endTime\r\n\r\n" + \
               "To print events\r\n" + \
               "=> /eventlist summary, maxResult"
        return text

if __name__ == '__main__':
    gcalendar = GCalendar('oraclian')
    # gcalendar.get_Calendar()
    # gcalendar.insert_Calendar(summary='연구실-개인 일정', body='Test', start='2017.09.15-06:00', end='2017.09.15-12:00')
    # gcalendar.insert_Calendar(summary='연구실-개인 일정', body='Test', start='2017.09.13', end='2017.09.14')
    # print(gcalendar.list_Calendar(summary='ejrgus94160@gmail.com', maxResult=5))
    # gcalendar.delete_Calendar(summary='연구실-개인 일정', event_summary='Test')
    # gcalendar.update_Calendar(summary='연구실-개인 일정', event_summary='Test', update_summary='Test Data')
    pass