from moviepy.editor import TextClip, CompositeVideoClip, AudioFileClip
import pyttsx3
import os

# Create text-to-speech audio
def generate_audio(text, output_path):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_path)
    engine.runAndWait()
    return output_path

# Create a single video
def create_video(topic, text, output_path):
    # Generate audio
    audio_path = generate_audio(text, f"{output_path}.mp3")

    # Create a text clip
    text_clip = TextClip(text, fontsize=50, color='white', size=(1280, 720), bg_color='black', method='caption')
    text_clip = text_clip.set_duration(30)  # 30-second clip

    # Add background music
    audio_clip = AudioFileClip(audio_path)
    text_clip = text_clip.set_audio(audio_clip)

    # Export video
    video_path = f"{output_path}.mp4"
    text_clip.write_videofile(video_path, fps=24, codec="libx264")
    return video_path

# Create videos for a topic
def create_videos(topic, count):
    video_paths = []
    for i in range(count):
        text = f"Video about {topic} - Part {i + 1}"
        output_path = f"videos/{topic.replace(' ', '_')}_{i + 1}"
        os.makedirs("videos", exist_ok=True)
        video_paths.append(create_video(topic, text, output_path))
    return video_paths