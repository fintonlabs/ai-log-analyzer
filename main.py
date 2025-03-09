import os
import time
from typing import List, Dict, Any
from collections import defaultdict

class LogAnalyzer:
    """
    A utility class to analyze system logs, detect anomalies, and summarize errors and patterns.
    """
    def __init__(self, log_file: str):
        """
        Initialize the LogAnalyzer with the path to the log file.
        """
        self.log_file = log_file
        self.anomalies = defaultdict(list)

    def read_logs(self) -> List[str]:
        """
        Read the log file and return a list of log lines.
        """
        try:
            with open(self.log_file, 'r') as file:
                logs = file.readlines()
            return logs
        except FileNotFoundError:
            print(f"Log file {self.log_file} not found.")
            return []
        except Exception as e:
            print(f"Error reading log file: {e}")
            return []

    def analyze_logs(self, logs: List[str]) -> Dict[str, Any]:
        """
        Analyze the logs and detect anomalies.
        """
        for log in logs:
            if "ERROR" in log:
                self.anomalies["errors"].append(log)
            elif "WARNING" in log:
                self.anomalies["warnings"].append(log)
        return self.anomalies

    def summarize(self) -> None:
        """
        Summarize the detected anomalies and errors.
        """
        print(f"Total errors: {len(self.anomalies['errors'])}")
        print(f"Total warnings: {len(self.anomalies['warnings'])}")

    def run(self) -> None:
        """
        Run the log analyzer.
        """
        logs = self.read_logs()
        self.analyze_logs(logs)
        self.summarize()


if __name__ == "__main__":
    log_analyzer = LogAnalyzer("system.log")
    log_analyzer.run()