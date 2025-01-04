import os
import time
from pathlib import Path
import shutil

# Directories to monitor
hf_format    = "/path/to/first/directory"
full_format  = "/path/to/second/directory"

# Time interval (in seconds) between checks
CHECK_INTERVAL = 5

def get_folders(directory):
    """Get a list of folders in the directory sorted by creation time."""
    return sorted(
        [f for f in Path(directory).iterdir() if f.is_dir()],
        key=lambda x: x.stat().st_ctime
    )

def keep_latest_folder(directory):
    """Ensure only the latest folder remains in the directory."""
    folders = get_folders(directory)
    if len(folders) == 0:
        return
    elif len(folders) > 1:
        for folder in folders[:-1]:
            shutil.rmtree(folder)
            print(f"Deleted folder: {folder}")

def monitor_directories(dir1, dir2):
    """Continuously monitor the directories."""
    while True:
        for directory in [dir1, dir2]:
            if os.path.exists(directory):
                keep_latest_folder(directory)
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor_directories(hf_format, full_format)

