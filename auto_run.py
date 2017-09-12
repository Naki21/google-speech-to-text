import os
from sys import argv
from goog import transcribe_gcs

def auto_run(directory):

    filenames = os.listdir(directory)
    for filename in filenames:
        os.rename(os.path.join(directory, filename), os.path.join(directory, filename.replace(' ', '')))

    for filename in os.listdir(directory):


        if filename.endswith(".mp4"):
            file_path = os.path.join(directory, filename)
            transcribe_gcs(file_path)
            print(file_path)
        else:
            continue

directory = argv[1]

auto_run(directory)