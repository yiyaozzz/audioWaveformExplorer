import subprocess
from pydub import AudioSegment
import os

def convert_mp4_to_mp3(mp4_file, mp3_file):
    command = ['ffmpeg', '-i', mp4_file, '-q:a', '0', '-map', 'a', mp3_file]
    subprocess.run(command, check=True)

def srt_time_to_seconds(time_str):
    hours, minutes, seconds = time_str.replace(',', '.').split(':')
    return int(hours) * 3600 + int(minutes) * 60 + float(seconds)

def segment_audio(audio_path, srt_path, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Load the full audio file
    audio = AudioSegment.from_file(audio_path)

    # Read the SRT file and split it into lines
    with open(srt_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Process the SRT file and segment the audio
    for i in range(0, len(lines), 4):  # Assuming each entry is 4 lines including the blank line
        index = lines[i].strip()
        times = lines[i + 1].strip()
        text = lines[i + 2].strip()
        start, end = times.split(' --> ')
        start_ms = srt_time_to_seconds(start) * 1000
        end_ms = srt_time_to_seconds(end) * 1000

        # Extract the segment from the audio
        segment = audio[start_ms:end_ms]

        # Export the segment as a separate audio file
        segment.export(f"{output_dir}/{index}_{start.replace(':', '').replace(',', '')}-{end.replace(':', '').replace(',', '')}.wav", format="wav")

# Main directories
audioProcess_dir = 'audioProcess'
os.makedirs(audioProcess_dir, exist_ok=True)

segments_dir = os.path.join(audioProcess_dir, 'segments')
os.makedirs(segments_dir, exist_ok=True)

# File paths
mp4_file = os.path.join(audioProcess_dir, 'sherlock.mp4')
mp3_file = os.path.join(audioProcess_dir, 'sherlock.mp3')
srt_file = os.path.join(audioProcess_dir, 'sherlockSub.srt')

# Convert MP4 to MP3
convert_mp4_to_mp3(mp4_file, mp3_file)

# Segment the audio
segment_audio(mp3_file, srt_file, segments_dir)
