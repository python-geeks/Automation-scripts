from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from task import Task
from datetime import timedelta, datetime


categories = {
    # Lavender
    '#a4bdfc': '',
    # Blueberry
    '#5484ed': '',
    # Peacock
    '#46d6db': 'Exercise',
    # Sage
    '#7ae7bf': 'My Apps',
    # Basil
    '#51b749': 'App',
    # Tangerine
    '#ffb878': '',
    # Banana
    '#fbd75b': '',
    # Flamingo
    '#ff887c': '',
    # Tomato
    '#dc2127': 'YouTube',
    # Mandarine
    '#fa573c': '',
    # Grape
    '#dbadff': 'Work',
    # Graphite
    '#e1e1e1': 'School'
}


EVENTS_TO_LOOK_THROUGH = 60
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
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
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    start_day = datetime.utcnow()
    now = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    last_monday = (datetime.utcnow()- timedelta(start_day.weekday())).isoformat() + 'Z' # 'Z' indicates UTC time
    week_end_time = str(datetime.utcnow() + timedelta(days=7)) + 'Z'
    print('Getting the upcoming 10 events')
    print('**************************************************************\n')
    events_result = service.events().list(calendarId='primary', timeMin=last_monday, timeMax=now, 
                                        maxResults=EVENTS_TO_LOOK_THROUGH, singleEvents=True,
                                        orderBy='startTime').execute()
    colors = service.colors().get(fields='event').execute()
    defaultColor = (service.calendarList().get(calendarId="primary").execute())['backgroundColor']
    events = events_result.get('items', [])
    tasks = []

    if not events:
        print('No upcoming events found.')
    for event in events:
        start_string = event['start'].get('dateTime', event['start'].get('date'))
        end_string = event['end'].get('dateTime', event['end'].get('date'))
        
        name = event['summary']
        try: 
            color = colors['event'][event['colorId']]['background']
        except KeyError:
            color = defaultColor
        task = Task(name, parse_time(start_string), parse_time(end_string), color)
        task.date = parse_time(start_string)
        task.get_time_of_task()
        tasks.append(task)
    
    total_tasks = []
    for color, category in categories.items():
        if len(category) > 1: 
            total_time = timedelta(hours=0)
            for task in tasks:
                if task.color == color:
                    total_time += task.total_time
            text = "For " + category + " you have planned to spend:"
            number_of_spaces = 15
            number_of_spaces -= len(category)
            string_length=len(text)+number_of_spaces    # will be adding 10 extra spaces
            string_revised=text.ljust(string_length)
            print("\n-----------------------------------------------------------------")
            print(string_revised + format_timedelta(total_time) + "hrs this week")
    print("\n-----------------------------------------------------------------\n")
    print("\n********************************************************\n")


def parse_time(timestamp):
    # Takes a timestamp string and returns a datetime object
    try:
        time_object = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S%z")
    except ValueError:
        # If no start and end time is specified the format string must be different
        time_object = datetime.strptime(timestamp, "%Y-%m-%d")
    return time_object


def format_timedelta(timedelta):
    # Takes a timedelta and returns a string
    hours = timedelta.total_seconds() / 3600
    return("%.2f" % hours)


if __name__ == '__main__':
    main()
