from pydub import AudioSegment
from pydub.playback import play
import pygame
import time

# Load the audio file
audio = AudioSegment.from_file("C:\\Users\\user\Music\\trev.mp3", format="mp3")

# Shift the pitch by +2 semitones
shifted_audio = audio._spawn(audio.raw_data, overrides={
    "frame_rate": int(audio.frame_rate * (2 ** (2 / 12.0)))
})

# Export the shifted audio to a new file
shifted_audio.export("shifted_music.mp3", format="mp3")

# Play the original audio
print("Playing original audio...")
play(audio)
time.sleep(audio.duration_seconds)  # Sleep to wait for audio playback to complete

# Play the shifted audio
print("Playing shifted audio...")
play(shifted_audio)
time.sleep(shifted_audio.duration_seconds)  # Sleep to wait for audio playback to complete
