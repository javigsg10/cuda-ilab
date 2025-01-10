import os
import time
from pathlib import Path
import shutil

# Directories to monitor
hf_format = "/root/.local/share/instructlab/checkpoints/hf_format"
full_state = "/root/.local/share/instructlab/checkpoints/full_state"

# Time interval (in seconds) between checks
CHECK_INTERVAL = 5

def get_folders(directory):
    """Get a list of folders in the directory sorted by creation time."""
    return sorted(
        [f for f in Path(directory).iterdir() if f.is_dir()],
        key=lambda x: x.stat().st_ctime
    )

def keep_latest_folder(directory):
    """Ensure only the latest folder remains in the directory if more than one exists."""
    folders = get_folders(directory)
    if len(folders) > 1:  # Only delete if there are more than one folder
        for folder in folders[:-1]:  # Keep the latest folder
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
    monitor_directories(hf_format, full_state)

