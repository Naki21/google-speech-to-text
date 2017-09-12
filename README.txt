Instructions for use

Use the Cloud Platform Console to create a new Cloud
Platform project, create an App Engine application, and
enable billing: https://console.cloud.google.com/
(Skip if project already set up)

Enable the Google Speech to Text API
in APIs and Services of new project

Set up a storage bucket in Google Cloud Storage


Download, install and set up Google SDK
https://cloud.google.com/sdk/
(authenticate your machine by following the auth instructions)


Set your virtual environment

If you don't have virtualenv, install it using pip.

    sudo pip install virtualenv

Create an isolated Python environment, and install dependencies:

virtualenv env
source env/bin/activate
pip install -r requirements.txt

Install ffmpeg
    sudo apt update
    sudo apt install ffmpeg

In goog.py change the bucket_name variable to the name of the storage bucket you wish to use

To run transcription script add .mp4 files to specified directory

Then run:

    python autorun.py /path/to/directory/

The script will automatically strip the audio files from the video and Convert them to .ogg format
The it uploads the audio to the gcloud storage bucket and
then passes its gcs_uri to the transcription API for processing

When finished, it outputs both the .srt formatted file and raw text file into the specified directory

Note that if the program errors, it terminates as to not potentially abuse any API quota limits