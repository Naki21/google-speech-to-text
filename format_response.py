import math
import json
import os
def format_transcript(results, audio_file):

    def format_time(seconds, offset=0):
        frac, whole = math.modf(seconds)
        f = frac * 1000
        m, s = divmod(whole, 60)
        h, m = divmod(m, 60)
        return "%d:%02d:%02d,%03d" % (h, m, s, (f + offset * 1000))


    # Create a function called "chunks" with two arguments, l and n:
    def chunks(l, n):
        # For item i in a range that is a length of l,
        for i in range(0, len(l), n):
            # Create an index range for l of n items:
            yield l[i:i + n]


    file = open( audio_file + ".srt", "w")
    counter = 0

    for result in results:
        print(result)
        alternatives = result.alternatives
        for alternative in alternatives:
            print(alternative)
            words = alternative.words
            print(words)

            if len(words) < 14:
                transcript = alternative.transcript
                start_time = words[0].start_time
                end_time = words[-1].end_time
                start_time_seconds = start_time.seconds + start_time.nanos * 1e-9

                end_time_seconds = end_time.seconds + end_time.nanos * 1e-9

                counter += 1

                file.write(str(counter) + '\n')
                file.write(format_time(start_time_seconds) + ' --> ' + format_time(end_time_seconds) + '\n')
                file.write(transcript + "\n\n")
            else:
                c = list(chunks(words, 14))
                for words in c:
                    start_time = words[0].start_time
                    end_time = words[-1].end_time

                    start_time_seconds = start_time.seconds + start_time.nanos * 1e-9

                    end_time_seconds = end_time.seconds + end_time.nanos * 1e-9

                    section = ''
                    for word_info in words:
                        section += word_info.word + " "

                    counter += 1
                    file.write(str(counter) + '\n')
                    file.write(format_time(start_time_seconds) + ' --> ' + format_time(end_time_seconds) + '\n')
                    file.write(section + "\n\n")
    file.close()
