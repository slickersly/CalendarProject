import sys
import pandas as pd
from oauth2client import client
from googleapiclient import sample_tools

eventList = []

def main(argv):
    # Authenticate and construct service.
    service, flags = sample_tools.init(
        argv, 'calendar', 'v3', __doc__, __file__,
        scope='https://www.googleapis.com/auth/calendar.readonly')

    try:
        page_token = None
        while True:
            events = service.events().list(calendarId='m7vcqfk2nvu1bscefu4najdm3g@group.calendar.google.com', pageToken=page_token).execute()
            #print(events) #test
            #input("Press enter to continue...")#test            
            for event in events['items']:
                eventList.append(event)
                print(str(event['summary']) + " " + str(event['start']) + " " + str(event['end']))
                #print(str(event['start']) + " " + str(event['end']))
            #    print(event['summary'])
            #    print(event)
            page_token = events.get('nextPageToken')
            if not page_token:
                break

    except client.AccessTokenRefreshError:
        print('The credentials have been revoked or expired, please re-run'
              'the application to re-authorize.')

if __name__ == '__main__':
    main(sys.argv)