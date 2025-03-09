import os
import time
import threading
from typing import List, Dict
from collections import defaultdict
from sklearn.ensemble import IsolationForest  # Hypothetical ML model

class LogMonitor:
    """
    A utility class to monitor and analyze system logs in real-time.
    """

    def __init__(self, log_dirs: List[str], alert_threshold: float):
        """
        Initialize the LogMonitor with directories to monitor and an alert threshold.
        """
        self.log_dirs = log_dirs
        self.alert_threshold = alert_threshold
        self.model = IsolationForest()  # Hypothetical ML model
        self.error_summary = defaultdict(int)
        self.alerts = []

    def monitor_logs(self):
        """
        Continuously monitor and read new entries in system log files.
        """
        while True:
            for log_dir in self.log_dirs:
                for filename in os.listdir(log_dir):
                    if filename.endswith(".log"):
                        self.process_log(os.path.join(log_dir, filename))
            time.sleep(1)  # Sleep for a second before checking for new logs

    def process_log(self, filepath: str):
        """
        Process a log file and update the error summary.
        """
        with open(filepath, 'r') as file:
            lines = file.readlines()
            for line in lines:
                anomaly_score = self.model.predict([line])  # Hypothetical ML model prediction
                if anomaly_score < self.alert_threshold:
                    self.error_summary[filepath] += 1
                    self.alerts.append(f"Alert: Anomaly detected in {filepath}")

    def get_summary(self) -> Dict[str, int]:
        """
        Return a summary of errors detected.
        """
        return self.error_summary

    def get_alerts(self) -> List[str]:
        """
        Return a list of alerts.
        """
        return self.alerts

# Example usage
if __name__ == "__main__":
    log_monitor = LogMonitor(["/var/log"], 0.5)
    threading.Thread(target=log_monitor.monitor_logs).start()  # Start monitoring logs in a new thread

    while True:
        print(log_monitor.get_summary())  # Print error summary every second
        time.sleep(1)