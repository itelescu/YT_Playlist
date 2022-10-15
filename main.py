
from local_files_ls import tracks_dir
from yt_search import video_id
from yt_playlist_creation import track_to_playlist
from time import sleep
from progress.spinner import MoonSpinner


# Select the path you want to investigate
path = r'C:\Users\itelescu'

# Progress bar animation
with MoonSpinner('Processing…') as bar:
    for i in range(100):
        sleep(0.05)
        bar.next()

for item in tracks_dir(path):
    print(f'{item} - {track_to_playlist(video_id(item))}')
