# IoT Service

<!-- ##설명 -->

`iotServer.py` 파일에 `MODEL`, `PORT`에 대한 정보를 넣고 적외선 LED가 달려있는 라즈베리파이에서 Python2로 돌립니다.



- - -
다음은 슬랙봇 command 정보입니다.

| Command | Request URL | Description | Hint |
| :------ | :---------- | :---------- | :--- |
| /ac-help| http://domain:port/iot-service/achelp | 명령어에 대해 도움말을 얻을 수 있습니다 | |
| /ac-on| http://domain:port/iot-service/acon | 에어컨을 켭니다 | (온도) |
| /ac-off| http://domain:port/iot-service/acoff | 에어컨을 끕니다 | |
| /ac-super| http://domain:port/iot-service/acsuper  | 파워냉방으로 설정합니다 | |
