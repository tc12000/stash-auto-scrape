import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from stash import stash
from config import config

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else config['watch_path']
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(config['wait_time'])
    finally:
        observer.stop()
        observer.join()


# called with filename every time new file is added
def main(path: str):
    # takes the local file path and makes it the union file path
    target_path = normalize_path(path)

    # tell stash the file exists, and to use it's metadata
    stash.metadata_scan([target_path])

    # todo: further data generation/performer data?


def normalize_path(path:str):
    if len(config['replace_path']) > 0 and len(config['replace_path_with']) > 0:
         return path.replace(config['replace_path'], config['replace_path_with'])

    return path