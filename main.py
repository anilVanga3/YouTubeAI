import schedule
import time
from topics import get_random_topics
from video_maker import create_videos
from uploader import upload_videos

# Schedule and orchestrate the daily tasks
def daily_task():
    topics = get_random_topics(2)  # Select 2 random topics
    print(f"Selected Topics: {topics}")
    
    video_paths = []
    for topic in topics:
        video_paths.extend(create_videos(topic, 2))  # Create 2 videos per topic
    
    upload_videos(video_paths)

# Schedule daily task at a specific time (e.g., 10 AM)
schedule.every().day.at("10:00").do(daily_task)

print("Video generator is running...")
while True:
    schedule.run_pending()
    time.sleep(1)