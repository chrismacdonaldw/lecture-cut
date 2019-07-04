# lecture-cut
lecture-cut is a personal project meant to hasten videos by trimming them based off of silent audio portions. Mostly meant for online lectures where professors take a long time to get to the point.

## Arguments
--output_file, type=str, default='out.mp4', help='name of file that will be output after trim'

--cut_interval, type=int, default=150, help='ms of silent audio segments to be cut to allow for a custom margin of error, default is 150'

--silence_threshold, type=int, default=-55, help='value in dBFS that when audio is lower then, will be considered silent. Default is -55'

## Requirements
- [FFmpeg](https://github.com/FFmpeg/FFmpeg)
- [Python3](https://www.python.org/downloads/)

## Credit
 - [PyDub](https://github.com/jiaaro/pydub/blob/master/README.markdown)

 PyDub made this entire thing a whole lot easier.
