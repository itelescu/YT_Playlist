
from googleapiclient.discovery import build
import os

'''Build function constructs a Resource object for interacting with an API. The serviceName and
version are the names from the Discovery service'''

'''In order to get API-key, it's needed to create a project on console.developers.google.com,
select the version of API (based on type of API there is different ways of auth) is required for the project.'''

# Hiding API_key in Environment Variables
api_key = os.environ.get('API_key')

# This function create a service object
youtube_service_obj = build('youtube', 'v3', developerKey=api_key)


def video_id(video_name):
    # Check if the track has a name
    if video_name is None or video_name == '':
        print('Track name is missing')
    else:
        # Make a request for required song name and ste up max-results to first search
        request = youtube_service_obj.search().list(
                                            part='snippet',
                                            maxResults=1,
                                            q=video_name)
    # Check the response and pass it forward to yt_playlist_creation.py file.
        response = request.execute()

        for item in response['items']:
            # Generate the video ID
            return item['id']['videoId']
