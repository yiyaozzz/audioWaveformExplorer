# Audio Processing and Visualization Tool

This project is designed to process an MP4 audio file and its corresponding subtitle (SRT) file. It includes two Python scripts: audioSegment.py and segmentVisual.py. The main objective is to convert the MP4 file to MP3, segment this MP3 file based on the subtitles, and then create visual waveform representations for each audio segment with corresponding textual labels.

## Requirements

Python 3.x
FFmpeg
PyDub (pip install pydub)
Pillow (pip install Pillow)
Subprocess (part of the standard Python library)

## Setup

### Downloading the MP4 File

Before running the scripts, please download the 'sherlock.mp4' file from the provided link and place it under the 'audioProcess' directory.

- Link: [sherlock.mp4](https://buckeyemailosu-my.sharepoint.com/:v:/g/personal/zhang_11896_buckeyemail_osu_edu/Ea_gW1flN9RJjQR0szNV0NEBG9b5AZGQ6734ZCTqejXPnA?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0RpcmVjdCJ9fQ&e=w8wkIg)

- Ensure you have placed the downloaded 'sherlock.mp4' and the corresponding SRT file ('sherlockSub.srt') in the 'audioProcess' directory.

## Usage

### audioSegment.py

This script is responsible for converting an MP4 file to an MP3 file and then segmenting it based on an SRT file.

#### Functionality:

1. Converts an MP4 file to an MP3 file using FFmpeg.
2. Segments the MP3 file into smaller parts based on the timestamps in the SRT file.
3. Exports each audio segment as a separate WAV file in the segments directory under audioProcess.

#### How to Run:

1. Ensure the MP4 file(sherlock.mp4) and the SRT file(sherlockSub.srt) are in the audioProcess directory.
2. Run the script: 'python audioSegment.py'
3. The MP3 conversion and audio segments will be saved in 'audioProcess' and 'audioProcess/segments', respectively.

### segmentVisual.py

This script generates waveform images for each audio segment created by 'audioSegment.py' and labels them with the corresponding text from the SRT file.

#### Functionality:

1. Generates waveform images for each audio segment.
2. Labels each waveform image with the corresponding subtitle text.
3. Saves the waveform images in 'audioProcess/waveform_images'.
4. Saves labeled waveform images in 'audioProcess/labeled_waveforms'.

#### How to Run:

1. After running 'audioSegment.py', execute 'segmentVisual.py'.
2. Waveform images will be saved in 'audioProcess/waveform_images'.
3. Labeled waveform images will be saved in 'audioProcess/labeled_waveforms'.

### Note on Temporary Files

During the execution of these scripts, temporary files (e.g., tempCodeRunnerFile.py) may be generated automatically by the scripts or the code execution environment. These files are typically used for intermediate processing and do not affect the final output. They can be ignored or deleted if no longer needed.
