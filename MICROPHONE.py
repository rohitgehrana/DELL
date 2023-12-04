import sounddevice as sd
import numpy as np

def record_microphone(pin=7, duration=5, fs=44100):
    print(f"Recording from microphone on pin {pin}...")
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    return audio_data

def play_audio(audio_data, fs=44100):
    print("Playing audio...")
    sd.play(audio_data, fs)
    sd.wait()
    print("Playback complete.")

if __name__ == "__main__":
    # Record audio from microphone
    recorded_data = record_microphone(pin=7, duration=5)

    # Play back the recorded audio through the speaker
    play_audio(recorded_data)
