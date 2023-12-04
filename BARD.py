import sounddevice as sd
from pydub import AudioSegment
from pydub.playback import play

def record_and_save_to_mp3(pin=7, duration=5, fs=44100, output_file="output.mp3"):
    print(f"Recording from microphone on pin {pin}...")
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()

    # Convert audio data to AudioSegment
    audio_segment = AudioSegment(
        audio_data.tobytes(),
        frame_rate=fs,
        sample_width=audio_data.dtype.itemsize,
        channels=1
    )

    # Save to MP3 file
    audio_segment.export(output_file, format="mp3")
    print(f"Audio recorded successfully. Saved to {output_file}")

    # Play back the recorded audio
    play(audio_segment)

if __name__ == "__main__":
    record_and_save_to_mp3(pin=7, duration=5)
