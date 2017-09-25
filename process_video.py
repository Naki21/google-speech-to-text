import subprocess

# Extract audio from video and compress audio
def process_video(video_file):

    def strip(text, suffix): # Strip .mp4 suffix from file name
        if not text.endswith(suffix):
            return text
        # else
        return text[:len(text) - len(suffix)]


    stripped_name = strip(video_file, ".mp4")
    audio_file = stripped_name + ".ogg"

    try:
        subprocess.call(["ffmpeg -i " + video_file + " -acodec libopus -ac 1 -ar 16000 -compression_level 10 -application voip -vn " + audio_file],  shell=True)
        return stripped_name

    except Exception as e:
        print(str(e))
        return

