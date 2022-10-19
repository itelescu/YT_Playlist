
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os
import time
from tqdm import trange
from time import sleep

credentials = None

# If credentials are saved in pickled file (from previous successful logins) in current directory,
# then we will load them in
if os.path.exists('token.pickle'):
    print('Loading Credentials ...')
    with open('token.pickle', 'rb') as token:
        credentials = pickle.load(token)

# If there are no valid credentials or those are missing then we will Request new one or will refresh for access token
if not credentials or not credentials.valid:
    if credentials and credentials.expired and credentials.refresh_token:
        print('Refreshing Access Token...')
        credentials.refresh(Request())
    else:
        print('Fetching New Tokens...')
        # This flow object will load in google OAuth2 credentials from client_secret file and select
        # the scopes of the information that app can access
        flow = InstalledAppFlow.from_client_secrets_file('client_secret.json',
                                                scopes=['https://www.googleapis.com/auth/youtube',
                                                         'https://www.googleapis.com/auth/youtube.force-ssl',
                                                         'https://www.googleapis.com/auth/youtube.upload',
                                                         'https://www.googleapis.com/auth/youtubepartner'])
        # Server Strategy of InstalledAppFlow:Flow object will help to run our local server,
        # so we can log into google account and allow access
        # to the script for accessing data (local server will get the authorization code which later will be
        # exchanged for a token)
        flow.run_local_server(port=8080, promt='consent')
        credentials = flow.credentials

        # Serialize credentials in a pickle file for future use
        with open('token.pickle', 'wb') as f:
            pickle.dump(credentials, f)

# This function create a service object
youtube_service_obj = build('youtube', 'v3', credentials=credentials)

# Encapsulate private channel ID into Environment variable
channel_id = os.environ.get('Youtube_account_ID')


def playlist_id():
    # Create playlist ID
    request = youtube_service_obj.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": "Music",
                "description": "Favorite playlist",
                "tags": [
                    "sample playlist",
                    "API call"
                ],
                "defaultLanguage": "en",
                "channelId": channel_id,
                "channelTitle": "Ion"
            },
            "status": {
                "privacyStatus": "private"
            }
        }
    )
    response = request.execute()

    return response['id']


new_playlist_id = playlist_id()


def track_to_playlist(track):

    request = youtube_service_obj.playlistItems().insert(
            part="snippet",
            body={
                "snippet": {
                    "playlistId": new_playlist_id,
                    "position": 0,
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": track
                        }
                    }
                }
            )
    start = time.time()
    response = request.execute()

    end_time = time.time()
    total_time = end_time - start

    for item in trange(int(total_time*100)):
        sleep(0.01)

    return f'Added to your youtube playlist in {total_time:0.2f} seconds'


if __name__ == '__main__':
    track_to_playlist()
