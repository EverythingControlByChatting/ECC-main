# Google Calendar Service

<!-- ##설명 -->
구글 캘린더 서비스 README.md입니다.

구글 캘린더 서비스를 이용하기 위해서는 먼저 [여기](https://console.developers.google.com/) 에서 Oauth2 인증정보를 생성하여야 합니다.

인증정보를 생성하고 json 파일을 생성하여 장고 폴더 안에 넣어주세요.

settings_secret.py 내부에 REDIRECT_URI 정보를 추가해 주세요.
- - -
다음은 슬랙봇 command 정보입니다.

| Command | Request URL | Hint |
| :------ | :---------- | :--- |
| /calendar-help | http://domain:port/calendar-service/calendar/help | |
| /calendar-list | http://domain:port/calendar-service/calendar/list | |
| /event-insert  | http://domain:port/calendar-service/event/insert  | summary, body, startTime, endTime |
| /event-delete  | http://domain:port/calendar-service/event/delete  | summary, event_summary |
| /event-update  | http://domain:port/calendar-service/event/update  | summary, event_summary, update_summary(, startTime, endTime) |
| /event-list    | http://domain:port/calendar-service/event/list    | summary, maxResult |