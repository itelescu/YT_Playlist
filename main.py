
from local_files_ls import tracks_dir
from yt_search import video_id
from yt_playlist_creation import track_to_playlist
from time import sleep
from progress.spinner import MoonSpinner

'''Based on search and adding items to playlist files, you can insert the path that needs to be investigated and 
according to folder name, user will receive options for parsing data'''


# Select the path you want to investigate
path = r'C:\Users\itelescu'

# Progress bar animation
with MoonSpinner('Processing…') as bar:
    for i in range(100):
        sleep(0.05)
        bar.next()

# Display found path(s) and show process progress along files_name
for file_name in tracks_dir(path):
    print(f'{file_name} - {track_to_playlist(video_id(file_name))}')
