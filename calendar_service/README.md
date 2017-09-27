# Google Calendar Service

<!-- ##설명 -->
구글 캘린더 서비스 README.md입니다.

구글 캘린더 서비스를 이용하기 위해서는 먼저 [여기](https://console.developers.google.com/) 에서 Oauth2 인증정보를 생성하여야 합니다.

인증정보를 생성하고 json 파일을 생성하여 장고 폴더 안에 넣어주세요.

settings_secret.py 내부에 REDIRECT_URI 정보를 추가해 주세요.
- - -
다음은 슬랙봇 command 정보입니다.

| Command | Request URL | Description | Hint |
| :------ | :---------- | :---------- | :--- |
| /calendar-help | http://domain:port/calendar-service/calendar/help | 캘린더 Helper입니다. | |
| /calendar-list | http://domain:port/calendar-service/calendar/list | 캘린더 목록을 출력합니다. | |
| /event-insert  | http://domain:port/calendar-service/event/insert  | 이벤트를 생성합니다. | calendar-name, text, startTime, endTime |
| /event-delete  | http://domain:port/calendar-service/event/delete  | 이벤트를 삭제합니다. | calendar-name, text |
| /event-update  | http://domain:port/calendar-service/event/update  | 이벤트를 수정합니다. | calendar-name, previous-text, update-text(, startTime, endTime) |
| /event-list    | http://domain:port/calendar-service/event/list    | 이벤트 목록을 출력합니다. | calendar-name, maxResult |

startTime과 endTime은 시작과 종료 시간을 의미합니다.
시간은 다음 두가지 방법으로 표현할 수 있습니다.
1. 2017.09.15-06:00
2. 2017.09.15