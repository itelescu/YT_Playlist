
import sys
import os

'''Search of tracks name in selected path.
1.Ask user to introduce needed path.
2.Search for files in chosen path by walking in all directories if that's the case.
3.Select only mp3 files and add them to the list.
4.Format each track name and prepare it for searching in youtube'''


def tracks_dir(base_path):
    # This function will provide all paths with indicated directory name
    folder_name = sys.argv[1]

    match_folders = []

    for (root, dirs, files) in os.walk(base_path):
        for item in dirs:
            if item == folder_name:
                # Once the provided name is matching with any directory name,
                # the path to that directory will be created and appended to 'math_folder' list
                match_folders.append(os.path.join(root, item))

    for path in match_folders:
        # Print all paths that can be found with provided directory name
        print(f'* {path}\n')

        # Ask user to select which path needs to be inspected further. '-1' is for accuracy of index
    selected_folder = int(input(
        'Choose the number of needed directory you want to inspect: ')) - 1

    list_of_tracks = []
    # Search for files in directory
    for (root, dirs, files) in os.walk(match_folders[selected_folder]):
        for item in files:
            if item.endswith('.mp3'):
                # Select only file names with '.mp3' in the end and remove this extension
                list_of_tracks.append(
                    item[:-4])
            else:
                continue
    # Output of this function will be list of strings with file names
    return list_of_tracks


if __name__ == '__main__':
    tracks_dir()
