import os
import shutil
from moviepy.editor import VideoFileClip, AudioFileClip

# Author: Jeba Seelan
# Topic: File Organizer Tool
# Created on: 2024-10-25
# Description: This script organizes files in a specified directory by sorting them into subfolders based on their types, such as Images, Documents, Videos, and Audio. It categorizes longer videos and audio tracks into dedicated folders for Movies and Song Playlists. The tool improves digital organization and simplifies file management.

def create_folders(directory, file_types):
    """Creates subfolders for each file type category."""
    for folder in file_types.keys():
        os.makedirs(os.path.join(directory, folder), exist_ok=True)

def move_file(file_path, target_folder):
    """Moves a file to the specified target folder."""
    try:
        shutil.move(file_path, target_folder)
        print(f"Moved: {file_path} to {target_folder}")
    except Exception as e:
        print(f"Error moving {file_path}: {e}")

def organize_files(directory):
    """Organizes files in the given directory into subfolders based on file types."""
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.docx', '.pptx', '.xlsx'],
        'Text Files': ['.txt'],
        'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
        'Audio': ['.mp3', '.wav', '.aac'],
        'Archives': ['.zip', '.tar', '.gz', '.rar'],
        'HTML': ['.html', '.htm'],
        'CSS': ['.css'],
        'JavaScript': ['.js'],
        'Python': ['.py'],
        'Java': ['.java'],
        'C': ['.c'],
        'C++': ['.cpp', '.hpp'],
        'PHP': ['.php'],
        'APKs': ['.apk'],
        'Executables': ['.exe'],
        'Movies': [],
        'Song Playlist': [],
        'Others': []
    }

    create_folders(directory, file_types)

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        if os.path.isdir(file_path):
            continue
        
        moved = False
        
        try:
            if filename.endswith('.mp4'):
                video = VideoFileClip(file_path)
                if video.duration > 3600:  # More than 1 hour
                    move_file(file_path, os.path.join(directory, 'Movies', filename))
                    moved = True
                video.close()
            elif filename.endswith('.mp3'):
                audio = AudioFileClip(file_path)
                if audio.duration > 600:  # More than 10 minutes
                    move_file(file_path, os.path.join(directory, 'Song Playlist', filename))
                    moved = True
                audio.close()

            if not moved:
                for folder, extensions in file_types.items():
                    if any(filename.lower().endswith(ext) for ext in extensions):
                        move_file(file_path, os.path.join(directory, folder, filename))
                        moved = True
                        break

            if not moved:
                move_file(file_path, os.path.join(directory, 'Others', filename))

        except Exception as e:
            print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    directory = input("Enter the path to the directory you want to organize: ")
    organize_files(directory)
    print("Files have been organized.")
