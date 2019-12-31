from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

from src.event_provider import EventProviderABC

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def get_credentials():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    # TODO: redo this as json (see from_authorized_user_file - is that the same
    # as just casting it to json?)
    if os.path.exists('authorized.json'):
        creds = Credentials.from_authorized_user_file('authorized.json')
    # If there are no (valid) credentials available, let the user log in.
    if not creds:
        if creds and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json',
                SCOPES,
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('authorized.json', 'w') as auth_file:
            auth_file.write(creds.to_json())

    return creds


class GoogleProvider(EventProviderABC):
    def find_events(self):
        credentials = get_credentials()
        service = build('calendar', 'v3', credentials=credentials)

        # Call the Calendar API
        # 'Z' indicates UTC time
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        events_result = service.events().list(
            calendarId='primary',
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy='startTime',
        ).execute()
        return events_result.get('items', [])
