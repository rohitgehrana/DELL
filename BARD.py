import pyaudio
import wave

# Set the chunk size to 1024 samples
CHUNK = 1024

# Open the output file in write binary mode
wf = wave.open('output.mp3', 'wb')

# Set the number of channels
wf.setnchannels(1)

# Set the sample width to 2 bytes
wf.setsampwidth(2)

# Set the frame rate to 44100 frames per second
wf.setframerate(44100)

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open an input stream
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=44100,
                input=True,
                frames_per_buffer=CHUNK)

# Start recording
print('Recording...')

# Read data from the stream and write it to the output file
data = stream.read(CHUNK)
while data != b'':
    wf.writeframes(data)
    data = stream.read(CHUNK)

# Stop recording
print('Recording stopped.')

# Stop the stream and close PyAudio
stream.stop_stream()
stream.close()
p.terminate()

# Close the output file
wf.close()

# Print a success message
print('Audio recorded successfully.')

