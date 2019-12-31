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
    """
    Pull Google oauth credentials from their source.

    As currently written, it looks for an `authorized.json` file
    that has current credentials, and if none exists, it pulls the
    user through an oauth flow through a local browser session.

    The resulting credentials are then saved for future runs,
    and on each run, the token is refreshed.
    """
    creds = None
    if os.path.exists('authorized.json'):
        creds = Credentials.from_authorized_user_file('authorized.json')
    # If there are no (valid) credentials available, let the user log in.
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
        """
        This method pulls credentials and makes a call to the Google API
        for the next ten events on the user's calendar.
        """
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
