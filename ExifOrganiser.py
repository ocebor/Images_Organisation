# Organize your photos and videos with this script
# Need EXIFTOOL to be used -> Please, change location and filename in script to make it work (line 30)
# Read.me for instructions


import os
import shutil
import subprocess
from datetime import datetime

def automate_workflow(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterate through all files in the source folder
    for file_name in os.listdir(source_folder):
        source_file_path = os.path.join(source_folder, file_name)
        
        # Skip directories
        if os.path.isdir(source_file_path):
            continue

        # Copy the file to the destination folder
        copied_file_path = os.path.join(destination_folder, file_name)
        shutil.copy2(source_file_path, copied_file_path)

        # Extract FileModifyDate using ExifTool
        try:
            result = subprocess.run(
                [r"C:\exiftool\exiftool.exe", "-FileModifyDate", "-d", "%Y/%Y%m%d/%Y%m%d", "-T", copied_file_path],
                capture_output=True, text=True, check=True
            )
            timestamp = result.stdout.strip()
            
            # Create the new file path with subfolders organized by date
            date_folder_path = os.path.join(destination_folder, os.path.dirname(timestamp))
            if not os.path.exists(date_folder_path):
                os.makedirs(date_folder_path)

            new_file_name = f"{os.path.basename(timestamp)}_{file_name}"
            new_file_path = os.path.join(date_folder_path, new_file_name)

            # Move the copied file to the new location
            shutil.move(copied_file_path, new_file_path)

        except subprocess.CalledProcessError as e:
            print(f"Failed to extract metadata for {file_name}: {e}")

if __name__ == "__main__":
    source_folder = input("Enter the source folder path: ")
    destination_folder = input("Enter the destination folder path: ")
    automate_workflow(source_folder, destination_folder)

