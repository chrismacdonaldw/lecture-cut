import subprocess
from pydub import AudioSegment
from pydub.silence import detect_silence

def extract_audio():
    filename = input("Enter filename: ")

    command = "ffmpeg -i " + filename + " -ab 160k -ac 2 -ar 44100 -vn cut.wav"
    subprocess.call(command, shell=True)

def analyze_audio():
    audio = AudioSegment.from_wav("cut.wav")
    return detect_silence(audio, silence_thresh = -50)

def get_chunk_lengths(audio_chunks):
      for chunk in audio_chunks:
          print(chunk)

extract_audio()
get_chunk_lengths(analyze_audio())