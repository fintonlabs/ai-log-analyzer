import os
import re
import time
import collections
from typing import Dict, List, Tuple
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class LogHandler(FileSystemEventHandler):
    """Handles log file changes."""

    def __init__(self, log_dir: str):
        self.log_dir = log_dir
        self.error_summary = collections.Counter()

    def on_modified(self, event):
        """Called when a file or directory is modified."""

        # Only process log files in the specified directory
        if event.src_path.startswith(self.log_dir) and event.src_path.endswith('.log'):
            self.process_log_file(event.src_path)

    def process_log_file(self, file_path: str):
        """Reads a log file and processes its contents."""

        with open(file_path, 'r') as file:
            for line in file:
                self.process_log_line(line)

    def process_log_line(self, line: str):
        """Processes a single line from a log file."""

        # Extract log level and message
        match = re.search(r'(\[INFO\]|\[WARNING\]|\[ERROR\]): (.*)', line)
        if match:
            log_level, message = match.groups()

            # If it's an error, add it to the summary
            if log_level == '[ERROR]':
                self.error_summary[message] += 1

    def print_error_summary(self):
        """Prints a summary of the errors."""

        print('Error summary:')
        for message, count in self.error_summary.items():
            print(f'{message}: {count}')

def monitor_logs(log_dir: str):
    """Monitors a directory for changes to log files."""

    event_handler = LogHandler(log_dir)
    observer = Observer()
    observer.schedule(event_handler, log_dir, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
            event_handler.print_error_summary()
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

if __name__ == '__main__':
    monitor_logs('/path/to/log/directory')