import os
import subprocess
from PIL import Image, ImageDraw, ImageFont

def srt_time_to_seconds(time_str):
    hours, minutes, seconds = time_str.replace(',', '.').split(':')
    return int(hours) * 3600 + int(minutes) * 60 + float(seconds)

def generate_waveform_for_segment(audio_segment_path, output_image_path):
    command = [
        'ffmpeg',
        '-i', audio_segment_path,
        '-filter_complex', 'showwavespic=s=1024x240',
        '-frames:v', '1',
        output_image_path
    ]
    subprocess.run(command, check=True)

def label_waveform_image(waveform_image_path, label_text, output_image_path):
    with Image.open(waveform_image_path) as image:
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()  # Replace with a path to a .ttf file if you want a different font
        text_position = (10, 10)  # Change as needed
        draw.text(text_position, label_text, font=font, fill='white')
        image.save(output_image_path)

# Ensure the directories for segments and waveforms exist
segments_dir = 'audioProcess/segments'
waveforms_dir = 'audioProcess/waveform_images'
labeled_waveforms_dir = 'audioProcess/labeled_waveforms'
os.makedirs(waveforms_dir, exist_ok=True)
os.makedirs(labeled_waveforms_dir, exist_ok=True)

# Read the SRT file and process each segment
srt_file_path = 'audioProcess/sherlockSub.srt'
with open(srt_file_path, 'r', encoding='utf-8') as file:
    srt_lines = file.readlines()

for i in range(0, len(srt_lines), 4):
    index = srt_lines[i].strip()
    times = srt_lines[i + 1].strip()
    text = srt_lines[i + 2].strip()

    start, end = times.split(' --> ')
    start_ms = srt_time_to_seconds(start) * 1000
    end_ms = srt_time_to_seconds(end) * 1000
    segment_filename = f"{index}_{start.replace(':', '').replace(',', '')}-{end.replace(':', '').replace(',', '')}.wav"
    waveform_image_filename = segment_filename.replace('.wav', '.png')
    
    audio_segment_path = os.path.join(segments_dir, segment_filename)
    waveform_image_path = os.path.join(waveforms_dir, waveform_image_filename)
    output_image_with_label_path = os.path.join(labeled_waveforms_dir, waveform_image_filename)

    generate_waveform_for_segment(audio_segment_path, waveform_image_path)
    label_waveform_image(waveform_image_path, text, output_image_with_label_path)
