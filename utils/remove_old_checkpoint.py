import os
import time
import shutil

def monitor_directory(directory_path):
    """
    Monitors the specified directory and ensures only the most recent folder remains.
    Deletes older folders if more than one is found.
    """
    while True:
        items = [os.path.join(directory_path, item) for item in os.listdir(directory_path)]
        folders = [item for item in items if os.path.isdir(item)]
        
        # If more than one folder exists, keep the most recent and delete the others
        if len(folders) > 1:
            # Sort folders by modification time (most recent last)
            folders.sort(key=lambda x: os.path.getmtime(x))
            
            # Keep the most recent folder
            most_recent = folders[-1]
            
            # Delete all other folders
            for folder in folders[:-1]:
                print(f"Deleting older folder: {folder}")
                shutil.rmtree(folder)
        
        # Wait for a short period before checking again
        time.sleep(5)  # Adjust the interval as needed

if __name__ == "__main__":
    directory_to_monitor = "/ruta/a/tu/directorio"  
    if not os.path.exists(directory_to_monitor):
        print(f"Error:  {directory_to_monitor} doesn't exist.")
    else:
        print(f"Monitoring: {directory_to_monitor}")
        monitor_directory(directory_to_monitor)

