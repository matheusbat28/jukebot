from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from decouple import config

youtube = build('youtube', 'v3', developerKey=config('YOUTUBE_API_KEY'))

def youtube_search(query):
    try:
        response = youtube.search().list(
            q=query,
            part='id',
            type='video',
            ).execute()
        video_id = response['items'][0]['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        return video_url
    except HttpError as e:
        print(f'o erro foi: {e}')           
