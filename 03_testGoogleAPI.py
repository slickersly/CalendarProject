import sys
import pandas as pd
from oauth2client import client
from googleapiclient import sample_tools

df = pd.DataFrame()


def main(argv):
    # Authenticate and construct service.
    service, flags = sample_tools.init(argv, 'calendar', 'v3', __doc__, __file__,scope='https://www.googleapis.com/auth/calendar.readonly')

    try:
        page_token = None
        while True:
            calendar_list = service.calendarList().get(calendarId='m7vcqfk2nvu1bscefu4najdm3g@group.calendar.google.com').execute()
            print(calendar_list['id'])
            if not page_token:
                break
    except client.AccessTokenRefreshError:
        print('The credentials have been revoked or expired, please re-run'
              'the application to re-authorize.')

if __name__ == '__main__':
    main(sys.argv)