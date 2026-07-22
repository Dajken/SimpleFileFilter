import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#file with extensions(config.py)
from config import EXTENSIONS

#Path to the Downloads folder and to the location where we want to sort.
DOWNLOADS = r"C:\Users\User\Downloads"#YOUR PATH TO DOWNLOADS
DESTINATION = r"C:\Users\User\Sort"#YOUR PATH TO SORTS(you can create one)

class Mover(FileSystemEventHandler):
    def on_created(self, event):
        #ignore directories
        if event.is_directory:
            return

        #file path, name and extension
        path = event.src_path
        name = os.path.basename(path)
        _, extension = os.path.splitext(name)

        #checking extension
        if extension.lower() in EXTENSIONS:
            folder_name = EXTENSIONS[extension.lower()]
            target = os.path.join(DESTINATION, folder_name)

            if not os.path.exists(target):
                os.makedirs(target)

            target_path = os.path.join(target, name)

            #move file
            try:
                time.sleep(1)
                shutil.move(path, target_path)
                print(f"file succesfully moved, {name} -> {folder_name}")
            except Exception as e:
                print(f"file cannot be moved {name}. {e}")

if __name__ == "__main__":
    print("Start...")

    event_mover = Mover()
    observer = Observer()

    #Watching downloads folder
    observer.schedule(event_mover, DOWNLOADS, recursive = False)
    observer.start()

    #Script running until stopped(ctrl+c)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Stop...")

    observer.join()