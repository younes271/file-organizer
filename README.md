# file-organizer
A new repository created via Python script


---

Sure, here's a basic Python script that will organize files on your desktop into folders based on their extension type.

```python
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
```

This script will create folders for each file type (e.g., .txt, .pdf, .jpg) on your desktop and move the corresponding files into these folders. Please note that this script is simplistic and doesn't handle exceptions or edge cases. It's recommended to back up your files before running it.