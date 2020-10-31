from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1dsVg0o9QRzP33gKLSYWQJtEDgY0Cx6fGgQvrMGnEdYM'
SAMPLE_RANGE_NAME = 'Auto Results!A2:F2'


def authgsheet():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

def send_to_sheets(elec_dem, elec_gop, sen_dem, sen_gop, hous_dem, hous_gop):
    creds = None
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    values = [[
        elec_dem, elec_gop, sen_dem, sen_gop, hous_dem, hous_gop
    ]]
    body = {
        "values": values
    }
    results = service.spreadsheets().values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                     range=SAMPLE_RANGE_NAME, valueInputOption="RAW", body=body).execute()