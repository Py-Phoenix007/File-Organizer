# File Organizer Tool

## Overview
The **File Organizer Tool** is a Python application that efficiently organizes files within a specified directory by categorizing them into subfolders based on their types. This tool helps declutter your digital workspace and enhances productivity.

## Features
- **Automated Organization**: Automatically sorts files into subfolders such as Images, Documents, Videos, Audio, and more.
- **Duration-Based Sorting**: Checks the duration of MP4 and MP3 files, moving longer files to dedicated 'Movies' and 'Song Playlist' folders.
- **Robust Error Handling**: Ensures smooth execution even when encountering file access issues.

## Requirements
- Python 3.x
- MoviePy library

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Py-Phoenix007/File-Organizer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd File-Organizer
   ```
3. Install the required dependencies:
   ```bash
   pip install moviepy
   ```

## Usage
1. Run the script:
   ```bash
   python file_organizer.py
   ```
2. Enter the path to the directory you wish to organize when prompted.

## Supported File Types
The script organizes files into the following categories:
- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`
- **Documents**: `.pdf`, `.docx`, `.pptx`, `.xlsx`
- **Text Files**: `.txt`
- **Videos**: `.mp4`, `.mkv`, `.avi`, `.mov`
- **Audio**: `.mp3`, `.wav`, `.aac`
- **Archives**: `.zip`, `.tar`, `.gz`, `.rar`
- **Others**: Any unrecognized file types are moved to the 'Others' folder.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For inquiries or collaboration, please reach out via GitHub or connect with me on LinkedIn : https://www.linkedin.com/in/jeba-seelan-598868324?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app
