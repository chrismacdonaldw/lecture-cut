import subprocess
import os
import argparse
from pydub import AudioSegment
from pydub.silence import detect_silence


def extract_audio():
    """
    Extracts audio from video file

    Returns:
        Returns filename for future use
    """
    filename = input("Enter filename: ")

    command = "ffmpeg -i " + filename + " -ab 160k -ac 2 -ar 44100 -vn cut.wav"
    subprocess.call(command, shell=True)
    return filename


def analyze_audio():
    """
    Finds silent chunks of audio

    Returns:
        Time intervals of silence
    """
    audio = AudioSegment.from_wav("cut.wav")
    return detect_silence(audio, silence_thresh=SILENCE_THRESHOLD)


def generate_command(silence, filename):
    """
    Generates FFmpeg Command to trim video
    using the aforementioned time intervals

    Args:
        silence: Intervals of silent audio
        filename: Filename given in extract_audio
    """
    videocmd = "ffmpeg -i " + filename + " -vf \"select='not("
    addcmd = ""
    for i, chunk in enumerate(silence):
        if i == 0:
            addcmd += 'between(t,%s,%s)' % (
                (chunk[0] + CUT_INTERVAL)/1000, (chunk[1] - CUT_INTERVAL)/1000)
        else:
            addcmd += '+between(t,%s,%s)' % (
                (chunk[0] + CUT_INTERVAL)/1000, (chunk[1] - CUT_INTERVAL)/1000)

    videocmd += '%s%s%s%s%s' % (
        addcmd,
        COMMAND_SET_ONE,
        addcmd,
        COMMAND_SET_TWO,
        OUTPUT_FILE
    )
    subprocess.Popen(videocmd, shell=False)


parser = argparse.ArgumentParser(
    description='Trims video based on segments which are under a specified silence threshold')
parser.add_argument('--output_file', type=str, default='out.mp4',
                    help='name of file that will be output after trim')
parser.add_argument('--cut_interval', type=int, default=150,
                    help='ms of silent audio segments to be cut to allow for a custom margin of error, default is 150')
parser.add_argument('--silence_threshold', type=int, default=-55,
                    help='value in dBFS that when audio is lower then, will be considered silent. Default is -55')
args = parser.parse_args()

OUTPUT_FILE = args.output_file
CUT_INTERVAL = args.cut_interval
SILENCE_THRESHOLD = args.silence_threshold
COMMAND_SET_ONE = ")',setpts=N/FRAME_RATE/TB\" -af \"aselect='not("
COMMAND_SET_TWO = ")',asetpts=N/SR/TB\" "


filename = extract_audio()
print(filename)
generate_command(analyze_audio(), filename)
os.remove('cut.wav')
