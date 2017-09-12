import os
from process_video import process_video
from upload_to_gcloud import upload_to_gcloud
from format_response import format_transcript

def transcribe_gcs(file_path):
    audio_file = process_video(file_path)

    bucket_name = 'test-dictation'
    print(file_path)
    file_name = os.path.basename(audio_file)
    print(file_name)

    upload_to_gcloud(bucket_name, source_file_name=audio_file + '.ogg', destination_blob_name=file_name + '.ogg')

    """Asynchronously transcribes the audio file specified by the gcs_uri."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()
    audio = types.RecognitionAudio(
        uri="gs://" + bucket_name + "/" + file_name + '.ogg')
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


    file = open( audio_file + '.txt', 'w')
    for result in results:
        for alternative in result.alternatives:
            file.write(alternative.transcript + '\n')
    file.close()

    format_transcript(results, audio_file)