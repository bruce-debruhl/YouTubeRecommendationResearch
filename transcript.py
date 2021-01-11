from youtube_transcript_api import YouTubeTranscriptApi

# turns a transcript from whatever dictionary YouTubeTranscriptApi
# gives us into a long string instead
# returns a string
def convertTranscript(transcript):
    res = ''
    for d in transcript:
        res = res + ' ' + d['text']
    return res


video_id = 'iFqEgu8hGJY'

transcript = YouTubeTranscriptApi.get_transcript(video_id)

transcript = convertTranscript(transcript)

print(transcript)
