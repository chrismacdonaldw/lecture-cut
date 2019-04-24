import subprocess
import pydub
from pydub import AudioSegment

def extract_audio():
    filename = input("Enter filename: ")

    command = "ffmpeg -i " + filename + " -ab 160k -ac 2 -ar 44100 -vn cut.wav"
    subprocess.call(command, shell=True)

def analyze_audio():
    audio = AudioSegment.from_wav("cut.wav")
    audio_chunks = pydub.silence.split_on_silence(audio, silence_thresh=-50)
    print("Chunks generated: ", audio_chunks)

def get_chunk_lengths():
    print("default")

extract_audio()
analyze_audio()