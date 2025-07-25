import os
from gtts import gTTS
from moviepy.editor import TextClip, AudioFileClip, CompositeVideoClip
from utils.lipsync import add_lip_sync

def generate_film(title, script):
    os.makedirs("films", exist_ok=True)

    # Generate speech audio
    tts = gTTS(text=script, lang='en')
    audio_path = f"films/{title}_audio.mp3"
    tts.save(audio_path)

    # Generate lip-sync video
    video_path = add_lip_sync(script, audio_path, title)

    return video_path