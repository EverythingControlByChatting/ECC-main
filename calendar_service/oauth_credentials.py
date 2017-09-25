#-*- coding:utf-8 -*-
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import os

try:
    import argparse
    flags = tools.argparser.parse_args([])
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'calendar_service/client_secret.json'
PROJECT_NAME = 'Google Calendar'

def oauth_credentials(origin_function):
    def decorator(*args, **kwargs):
        print("user_id: {}".format(args[0]))

        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
                os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir, args[0]+'.json')
        store = Storage(credential_path)
        credentials = store.get()

        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, scope=SCOPES, redirect_uri="http://5pecia1.iptime.org:18000/calendar-service/calendar/redirect")
            flow.user_agent = PROJECT_NAME
            flow.params['access_type'] = 'offline'

            auth_uri = flow.step1_get_authorize_url()
            
            return auth_uri+'&state='+args[0]
        return credentials
    return decorator