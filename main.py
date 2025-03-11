import os
import time
import threading
from typing import List, Dict
from collections import defaultdict

class LogAnalyzer:
    """
    A class used to analyze system logs and detect anomalies.

    ...

    Attributes
    ----------
    log_files : list
        a list of log files to be analyzed
    error_patterns : list
        a list of error patterns to be detected
    error_summary : dict
        a dictionary to store the summary of detected errors

    Methods
    -------
    analyze_logs():
        Analyzes the log files and detects anomalies.
    generate_report():
        Generates a daily report summarizing all the anomalies and errors detected.
    """

    def __init__(self, log_files: List[str], error_patterns: List[str]):
        """
        Constructs all the necessary attributes for the LogAnalyzer object.

        Parameters
        ----------
            log_files : list
                a list of log files to be analyzed
            error_patterns : list
                a list of error patterns to be detected
        """

        self.log_files = log_files
        self.error_patterns = error_patterns
        self.error_summary = defaultdict(int)

    def analyze_logs(self):
        """Analyzes the log files and detects anomalies."""

        def tail_log_file(log_file: str):
            """Helper function to tail a log file in real-time."""

            with open(log_file, 'r') as file:
                file.seek(0, 2)
                while True:
                    line = file.readline()
                    if not line:
                        time.sleep(0.1)
                        continue
                    yield line

        def analyze_log_file(log_file: str):
            """Helper function to analyze a log file."""

            for line in tail_log_file(log_file):
                for pattern in self.error_patterns:
                    if pattern in line:
                        self.error_summary[pattern] += 1
                        print(f"Alert: Detected '{pattern}' in {log_file}")

        # Start a new thread for each log file
        for log_file in self.log_files:
            if not os.path.exists(log_file):
                print(f"Error: {log_file} does not exist")
                continue
            threading.Thread(target=analyze_log_file, args=(log_file,)).start()

    def generate_report(self):
        """Generates a daily report summarizing all the anomalies and errors detected."""

        report_file = "error_report.txt"
        with open(report_file, 'w') as file:
            for pattern, count in self.error_summary.items():
                file.write(f"{pattern}: {count}\n")
        print(f"Daily error report has been saved to {report_file}")


# Example usage
log_files = ["system.log", "application.log"]
error_patterns = ["Error", "Failure", "Critical"]
analyzer = LogAnalyzer(log_files, error_patterns)
analyzer.analyze_logs()

# Generate a daily report every 24 hours
while True:
    time.sleep(24 * 60 * 60)
    analyzer.generate_report()