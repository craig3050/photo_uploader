from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import requests

# Setup the Photo v1 API
SCOPES = 'https://www.googleapis.com/auth/photoslibrary'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('creds.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('photoslibrary', 'v1', http=creds.authorize(Http()))

def list_albums():
    # Call the Photo v1 API
    results = service.albums().list(pageSize=50, fields="nextPageToken,albums(id,title)").execute()
    items = results.get('albums', [])
    if not items:
        print('No albums found.')
    else:
        print('Albums:')
        for item in items:
            print('{0} ({1})'.format(item['title'].encode('utf8'), item['id']))

def list_albums2():
        results = requests.get('https://photoslibrary.googleapis.com/v1/albums')
        results_json = results.json()
        print(results_json)

def create_album(name):
    # Create an album
    #results = service.albums().create(fields="album(test)").execute()
    pass



if __name__ == '__main__':
    list_albums2()
    #create_album("test")