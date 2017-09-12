
"""Sample code to use the IBM Watson Speech to Text API.
See more at https://blog.rmotr.com.
"""
from sys import argv
import subprocess
# from format_test import format_transcript
import os


def strip(text, suffix):
    if not text.endswith(suffix):
        return text
    # else
    return text[:len(text) - len(suffix)]


def process_video(file_path):
    video_file = file_path


    stripped_name = strip(video_file, ".mp4")
    stripped_file = strip(video_file, '.mp4') + ".ogg"

    subprocess.call(["ffmpeg -i " + video_file + " -acodec libopus -ac 1 -ar 16000 -compression_level 10 -application voip -vn " + stripped_file],  shell=True,)

    return stripped_name

