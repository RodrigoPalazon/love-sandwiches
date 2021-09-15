import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
print(CREDS)
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
print(SCOPED_CREDS)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
print(GSPREAD_CLIENT)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')
print(SHEET)

