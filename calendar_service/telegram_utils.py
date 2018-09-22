import requests
import settings_secret

TOKEN = settings_secret.TELEAGRAM_TOKEN

def send_message(text, chat_id):
    url = "https://api.telegram.org/bot{0}/sendMessage".format(TOKEN)
    data = {'chat_id' : chat_id, 'text' : text}
    response = requests.post(url, data=data)
    print(response.content)