from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle

# Authenticate with YouTube API
def authenticate_youtube():
    SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    return build("youtube", "v3", credentials=creds)

# Upload a single video
def upload_video(video_file, title, description):
    youtube = authenticate_youtube()
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "tags": ["daily", "auto-generated", "updates"],
                "categoryId": "22"  # Category 22 = People & Blogs
            },
            "status": {
                "privacyStatus": "public"
            }
        },
        media_body=MediaFileUpload(video_file)
    )
    response = request.execute()
    print(f"Uploaded {video_file}: {response['id']}")

# Upload multiple videos
def upload_videos(video_paths):
    for video_path in video_paths:
        title = os.path.basename(video_path).replace("_", " ").replace(".mp4", "").title()
        description = f"This video is about {title}. Auto-generated daily."
        upload_video(video_path, title, description)