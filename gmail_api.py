from __future__ import print_function

import os.path
from base64 import urlsafe_b64decode, urlsafe_b64encode
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def base64UrlEncode(data):
    return urlsafe_b64encode(data).rstrip(b'=')
def base64UrlDecode(base64Url):
    padding = b'=' * (4 - (len(base64Url) % 4))
    return urlsafe_b64decode(base64Url + padding)

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('gmail', 'v1', credentials=creds)
        results = service.users().messages().list(userId='me').execute()
        emails = results.get('messages')

        if not emails:
            print('No emails found.')
            return
        #get last email sent by iphone's shortcut
        txt = service.users().messages().get(userId='me', id=emails[0]['id']).execute()
        text = txt['payload']['body']['data']
        base64Url = base64UrlDecode(text.encode('utf-8')).decode('utf-8')
        base64Url = base64Url.replace('&amp;apos;',"'")
        logs = base64Url.split('<br/>')
        from datetime import date
        name = str(date.today())+'.csv'
        with open(name, 'w') as f:
            f.write("Action;Subject;Number;Time;Location\n")
        with open(name, 'a') as f:
            f.write(''.join(logs))

    except HttpError as error:
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()