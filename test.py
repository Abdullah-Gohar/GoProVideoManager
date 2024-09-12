import subprocess
from datetime import datetime
from moviepy.editor import VideoFileClip

def parse_creation_date(date_str):
    # Extract the date and time part from the string (2024:09:06 17:59:49)
    # The date format is 'YYYY:MM:DD HH:MM:SS'
    date_part = date_str.split(": ", 1)[1].strip()

    # Convert to datetime object using the format 'YYYY:MM:DD HH:MM:SS'
    creation_datetime = datetime.strptime(date_part, '%Y:%m:%d %H:%M:%S')

    # Convert datetime object to the number of seconds since the epoch
    epoch_time = creation_datetime.timestamp()

    return epoch_time

def get_video_creation_time(file_path):
    # Run the ExifTool command to get all metadata
    result = subprocess.run(['exiftool', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Capture the output from ExifTool
    output = result.stdout
    
    # Loop through each line to find the creation time (typically under "Create Date" or "Media Create Date")
    for line in output.splitlines():
        if "Create Date" in line or "Media Create Date" in line:
            print(line)
            return line
    
    return "Creation date not found"

def get_duration(file_path):
    video = VideoFileClip(file_path)

    # Get the duration in seconds
    duration = video.duration
    
    return duration



import os

def list_files_in_folder(folder_path):
    # Get a list of all files and directories in the folder
    all_files = os.listdir(folder_path)

    # Filter out directories to only include files
    files = [f for f in all_files if os.path.isfile(os.path.join(folder_path, f))]

    return files

import os
import shutil

def create_folders_and_move_files(source_folder, destination_folder, folder_prefix):
    # Get a list of all MP4 files in the source folder
    mp4_files = [f for f in os.listdir(source_folder) if f.endswith('.mp4')]
    
    for file_name in mp4_files:
        # Create a folder based on a naming pattern (e.g., "Folder_1", "Folder_2", ...)
        folder_name = f"{folder_prefix}_{mp4_files.index(file_name) + 1}"
        folder_path = os.path.join(destination_folder, folder_name)
        
        # Create the folder if it does not exist
        os.makedirs(folder_path, exist_ok=True)
        
        # Move the file to the created folder
        source_file_path = os.path.join(source_folder, file_name)
        destination_file_path = os.path.join(folder_path, file_name)
        shutil.move(source_file_path, destination_file_path)
        
        print(f"Moved {file_name} to {folder_path}")
        
from collections import defaultdict

def group_by_attribute(data, index):
    grouped = defaultdict(list)
    
    for item in data:
        key = item[index]
        grouped[key].append(item)
    
    return dict(grouped)

# Example usage
# source_folder = r"C:\path\to\source\folder"
# destination_folder = r"C:\path\to\destination\folder"
# folder_prefix = "Folder"  # Base name for folders

# create_folders_and_move_files(source_folder, destination_folder, folder_prefix)


# file_path = "G:\GoPro Vids\GX060060.MP4"
# creation_date = get_video_creation_time(file_path)

files = list_files_in_folder("G:\GoPro Vids")
files  = [os.path.join("G:\GoPro Vids", file) for file in files]
# files = ["G:\GoPro Vids\GX060060.MP4", "G:\GoPro Vids\GX070060.MP4","G:\GoPro Vids\GX080060.MP4"]
prev = 0
creation_dates = []
for file_path in files:
    if not file_path.endswith(".MP4"):
        continue
    creation_date = get_video_creation_time(file_path)
    epoch = parse_creation_date(creation_date)
    creation_date = creation_date.split(": ",1)[1].strip()
    
    creation_dates.append([file_path,creation_date,epoch])
    # duration = get_duration(file_path)
    
    # print(f"Duration: {duration}")
    # print(f"Epoch Time: {parse_creation_date(creation_date)}")
    # print("Time difference: ", parse_creation_date(creation_date) - prev)
    # prev = parse_creation_date(creation_date)

creation_dates.sort(key=lambda x: x[1])
for file in creation_dates:
    print(file)
    
    
creation_dates = group_by_attribute(creation_dates, 1)

import json
print(json.dumps(creation_dates, indent=4))

with open("data.json",'w',encoding='utf-8') as f:
    json.dump(creation_dates,f,indent=4)