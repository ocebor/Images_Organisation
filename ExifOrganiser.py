# Organize your photos and videos with this script
# Need EXIFTOOL to be used -> Please, change location and filename in script to make it work (line 27)
# Read.me for instructions


import os
import shutil
import subprocess
from datetime import datetime

def automate_workflow(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Walk through all files and subfolders in the source folder
    for root, _, files in os.walk(source_folder):
        for file_name in files:
            source_file_path = os.path.join(root, file_name)

            # Copy the file to the destination folder (ignore source structure)
            copied_file_path = os.path.join(destination_folder, file_name)
            shutil.copy2(source_file_path, copied_file_path)

            # Extract CreateDate using ExifTool
            try:
                result = subprocess.run(
                    [r"c:\exiftool\exiftool.exe", "-CreateDate", "-d", "%Y/%Y%m%d/%Y%m%d_%H%M%S", "-T", copied_file_path],
                    capture_output=True, text=True, check=True
                )
                timestamp = result.stdout.strip()

                # Verify if timestamp is valid
                if not timestamp:
                    raise ValueError("No valid timestamp extracted")

                # Create the new file path with subfolders organized by date
                date_folder_path = os.path.join(destination_folder, os.path.dirname(timestamp))
                if not os.path.exists(date_folder_path):
                    os.makedirs(date_folder_path)

                new_file_name = f"{os.path.basename(timestamp)}_{file_name}"
                new_file_path = os.path.join(date_folder_path, new_file_name)

                # Move the copied file to the new location
                shutil.move(copied_file_path, new_file_path)

            except (subprocess.CalledProcessError, ValueError) as e:
                print(f"Failed to extract metadata for {file_name}: {e}")
                # Use the current timestamp as a fallback
                fallback_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                fallback_file_name = f"{fallback_timestamp}_{file_name}"
                fallback_file_path = os.path.join(destination_folder, fallback_file_name)
                shutil.move(copied_file_path, fallback_file_path)

    print("Workflow completed successfully!")

if __name__ == "__main__":
    source_folder = input("Enter the source folder path: ")
    destination_folder = input("Enter the destination folder path: ")
    automate_workflow(source_folder, destination_folder)
