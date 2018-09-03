# Everything Control by Chatting

<!-- ## 서문 -->
**ECC**는 누구나 쉽게 접근 가능하고 사용 가능한 채팅이라는 플랫폼을 이용해서 에어컨, 도어락, 입출입관리 등의 사물이나 G Suite, Github, Trello, MS Office 등의 프로그램을 제어하고 관리하는 서비스를 만드는 프로젝트 입니다. 

채팅을 관리하는 서버 외에 사물, 외부 프로그램을 관리하는 서버를 각각 두어 MSA(Micro Service Architecture)방식으로 개발하는 것을 지향하며 안전하고 쉬운 설치와 사용을 위해 Dokcer Image를 만들어 배포할 예정 입니다.


## Getting Started

### Prerequisites

* Python3
* Raspberry Pi
  - Python2.7
  - Infrared sensor

### Installing

1. clone project
    ```bash
    git clone https://github.com/5pecia1/ECC-main.git
    ```
2. cd & install requirements
    ```bash
    cd ECC-main
    pip3 install -r requirements.txt
    ```

### Service 

각 서비스 설정법은 링크를 참고하세요.

* [Sample](https://github.com/5pecia1/ECC-main/tree/master/sample/README.md)
* [Google Calender](https://github.com/5pecia1/ECC-main/blob/master/calendar_service/README.md)
* [Air Conditioner Control](https://github.com/5pecia1/ECC-main/tree/master/iot_service/README.md)
* [Lunch Search](https://github.com/5pecia1/ECC-main/blob/master/chat_service/README.md)

### Slack 

1. [Create new app](https://api.slack.com/apps)
2. Set slack app
3. make slash command

### Project 

1. make `settings_secret.py`
    ```python
    SLACK_APP_TOKEN = # Install App -> OAuth Access Token
    SLACK_VERIFICATION_TOKEN = # Basic Information -> Verification Token
    
    SLACK_CLIENT_ID = # Basic Information -> Client ID
    SLACK_CLIENT_SECRET = # Basic Information -> Client Secret
    TEST_ADDRESS = # Django host:port name
    
    HOST = # Raspberry Pi host
    PORT = # Raspberry Pi port
    
    REDIRECT_URI = # Google App Redirect Uri
    ```

## Running

1. run server
    ```bash
    python3 manage.py runserver 0.0.0.0:8000
    ```
2. install slack app(Authorize)
    
    http://serverDomain:port/main/slack/add

    * DisallowedHost at /main/slack/add 뜰 경우 해결 방법
      - https://github.com/EverythingControlByChatting/ECC-main/issues/34

    * serverDomain이 없으면 본인 IP주소 입력

3. set Redirect URLs
   -  add http://serverDomain:port/main/slack/oauth
