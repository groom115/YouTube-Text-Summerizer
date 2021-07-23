def get_transcript(url):
  
  from youtube_transcript_api import YouTubeTranscriptApi

  youtube_vid = url
  video_id = youtube_vid.split("watch?v=")
  video_id = video_id[1]
  YouTubeTranscriptApi.get_transcript(video_id)
  trans = YouTubeTranscriptApi.get_transcript(video_id)
  text = ""
  for i in trans:
    text += ' ' + i['text']
  #print(text)
 # print(len(text))
  return text
