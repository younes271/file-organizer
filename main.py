import os
from pathlib import Path

DESKTOP_PATH = Path(os.path.join(os.path.expanduser("~"), "Desktop"))

def organize_directory(directory_path):
    for item in directory_path.iterdir():
        if item.is_file():
            file_path = Path(directory_path / item.name)
            file_format = file_path.suffix.lower()

            directory = directory_path / file_format
            directory.mkdir(exist_ok=True)

            file_path.rename(directory / file_path.name)

organize_directory(DESKTOP_PATH)
