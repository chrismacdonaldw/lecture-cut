import subprocess
import os
from pydub import AudioSegment
from pydub.silence import detect_silence

def extract_audio():
    filename = input("Enter filename: ")

    command = "ffmpeg -i " + filename + " -ab 160k -ac 2 -ar 44100 -vn cut.wav"
    subprocess.call(command, shell=True)
    return filename

def analyze_audio():
    audio = AudioSegment.from_wav("cut.wav")
    return detect_silence(audio, silence_thresh = -55)

def generate_command(silence, filename):
    videocmd = "ffmpeg -i " + filename + " -vf \"select='not("
    setadd = ""
    for i, chunk in enumerate(silence):
        if i == 0:
            setadd += 'between(t,%s,%s)' % ((chunk[0] + 150)/1000, (chunk[1] - 150)/1000)
        else:
            setadd += '+between(t,%s,%s)' % ((chunk[0] + 150)/1000, (chunk[1] - 150)/1000)
    
    videocmd += setadd
    videocmd += ")',setpts=N/FRAME_RATE/TB\" -af \"aselect='not("
    videocmd += setadd
    videocmd += ")',asetpts=N/SR/TB\" out.mp4"
    print(videocmd)
    subprocess.call(videocmd, shell=True)


filename = extract_audio()
generate_command(analyze_audio(), filename)