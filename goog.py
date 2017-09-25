import os
from process_video import process_video
from upload_to_gcloud import upload_to_gcloud
from format_response import format_transcript
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

def transcribe_gcs(mp4_file):
    audio_file_path = process_video(mp4_file) #Create audio file

    if audio_file_path:
        bucket_name = 'test-dictation' # Your gcloud bucket name
        print(mp4_file)
        audio_file_name = os.path.basename(audio_file_path) + '.ogg'
        print(audio_file_name)

        upload_to_gcloud(bucket_name, source_file_name=audio_file_path + '.ogg', destination_blob_name=audio_file_name)

        """Asynchronously transcribes the audio file specified by the gcs_uri."""

        client = speech.SpeechClient()
        audio = types.RecognitionAudio(
            uri="gs://" + bucket_name + "/" + audio_file_name)
        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.OGG_OPUS,
            language_code='en-US',
            sample_rate_hertz=16000,
            enable_word_time_offsets=True
        )
        operation = client.long_running_recognize(config, audio)

        if not operation.done():
            print('Waiting for results...')

        result = operation.result()


        results = result.results

        raw_text_file = open( audio_file_path + '.txt', 'w')
        for result in results:
            for alternative in result.alternatives:
                raw_text_file.write(alternative.transcript + '\n')
        raw_text_file.close() #output raw text file of transcription

        format_transcript(results, audio_file_path) #output .srt formatted version of transcription
    else:
        return

