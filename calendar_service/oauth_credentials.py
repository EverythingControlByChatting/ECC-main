#-*- coding:utf-8 -*-
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from ECC_main import settings
import os
import settings_secret

try:
    import argparse
    flags = tools.argparser.parse_args([])
except ImportError:
    flags = None

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
            flow = client.flow_from_clientsecrets(settings.CLIENT_SECRET_FILE, scope=settings.SCOPES, redirect_uri=settings_secret.REDIRECT_URI)
            flow.user_agent = settings.PROJECT_NAME
            flow.params['access_type'] = 'offline'

            auth_uri = flow.step1_get_authorize_url()
            
            return auth_uri+'&state='+args[0]
        return credentials
    return decorator