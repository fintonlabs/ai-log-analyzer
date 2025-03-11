# A Python utility that uses AI to analyze system logs and detect anomalies, summarizing errors and patterns in real-time


## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [📋 Table of Contents](#📋-table-of-contents)
- [Prerequisites](#prerequisites)
- [Installation Process](#installation-process)
- [Verification Steps](#verification-steps)
- [Post-Installation Configuration](#post-installation-configuration)
- [1. Basic Usage Examples](#1.-basic-usage-examples)
- [2. Common Use Cases](#2.-common-use-cases)
- [3. Command-line Arguments or Parameters](#3.-command-line-arguments-or-parameters)
- [4. Expected Output Examples](#4.-expected-output-examples)
- [5. Advanced Usage Scenarios](#5.-advanced-usage-scenarios)
- [Class: LogAnalyzer](#class:-loganalyzer)
- [Best Practices](#best-practices)
- [Common Patterns](#common-patterns)
- [Error Handling](#error-handling)
- [⚙️ Configuration](#⚙️-configuration)
- [🔍 Troubleshooting](#🔍-troubleshooting)
- [🤝 Contributing](#🤝-contributing)
- [📄 License](#📄-license)
- [API Documentation](#api-documentation)
## Overview

This project revolves around a Python utility, known as `LogAnalyzer`, developed to utilize Artificial Intelligence (AI) for the purpose of analyzing system logs and detecting anomalies. The `LogAnalyzer` class can parse through multiple log files, identify error patterns, and provide real-time summaries of detected anomalies. This tool is exceptionally useful for system administrators and developers who need to monitor system logs for errors or unusual activities, allowing them to promptly address potential issues before they escalate.

## Features

- **Log File Analysis** :mag: 

  The `LogAnalyzer` can be configured to analyze multiple log files. Users simply need to provide a list of log files during the initialization of the `LogAnalyzer` object. This can be extremely useful in environments where logs are distributed across multiple files or systems.

- **Error Pattern Detection** :warning: 

  This utility is not limited to identifying explicit errors but can detect specific patterns of errors. During the initialization of the `LogAnalyzer`, users can provide a list of error patterns to be identified. This feature allows users to monitor recurring issues or specific patterns that could signify a larger problem.

- **Real-time Anomaly Detection** :clock3: 

  The `LogAnalyzer` is designed to analyze logs in real time. This allows for immediate detection and reporting of errors or anomalies, enabling quick response times to system issues.

- **Error Summary** :bar_chart: 

  `LogAnalyzer` maintains a dictionary that holds a summary of detected errors. This feature provides an organized structure for storing and retrieving error summaries, making it easier for users to understand the frequency and types of errors occurring in the system.

- **Daily Report Generation** :page_with_curl: 

  The `generate_report()` method allows the `LogAnalyzer` to produce daily reports summarizing all detected anomalies and errors. This feature is particularly handy for system administrators who require a daily overview of system health.

- **Thread-Safety** :lock: 

  The `LogAnalyzer` uses threading, which allows it to safely analyze multiple log files concurrently. This improves the efficiency of the system, particularly when dealing with a large number of log files.

- **Modular and Scalable Design** :arrow_up_small: 

  The `LogAnalyzer` is designed with a modular approach, making it easy to extend its functionality. For example, new methods for different types of analysis can be added to the `LogAnalyzer` class without affecting existing functionalities.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

# Installation Instructions for Python Log Analyzer

This guide provides comprehensive instructions on how to install and configure the Python Log Analyzer, a utility for analyzing system logs and detecting anomalies.

## Prerequisites

Before you begin, ensure that you have the following installed on your machine:

- Python (3.7 or later): If not already installed, you can download Python from the official [Python download page](https://www.python.org/downloads/)
- pip (Python package installer): pip is usually installed with Python. If not, follow the instructions [here](https://pip.pypa.io/en/stable/installation/).

Additionally, you need to install the following Python libraries:

- os
- time
- threading
- typing
- collections

These libraries come pre-installed with Python, so you don't need to install them separately.

## Installation Process

Follow these steps to install the Python Log Analyzer:

1. **Clone the Repository:**

    Open a terminal and navigate to the directory where you want to clone the repository. Run the following command:

    ```bash
    git clone https://github.com/your-repo-url/python-log-analyzer.git
    ```

2. **Navigate to the Project Directory:**

    Change the directory to the cloned repository:

    ```bash
    cd python-log-analyzer
    ```

3. **Install the Project:**

    As the project does not have any external dependencies, no further installation steps are required.

## Verification Steps

To verify that the Python Log Analyzer has been installed correctly, perform the following steps:

1. Run the Python script:

    ```bash
    python log_analyzer.py
    ```

2. If the script runs without any errors, the installation was successful.

## Post-Installation Configuration

After installation, you need to configure the Python Log Analyzer to specify which log files to analyze and what error patterns to detect.

1. Open the `log_analyzer.py` file in a text editor.
2. In the `__main__` section at the end of the file, set the `log_files` variable to a list of your log files and `error_patterns` to a list of error strings to detect:

    ```python
    if __name__ == "__main__":
        log_files = ["path/to/your/logfile1", "path/to/your/logfile2"]
        error_patterns = ["error", "failure", "critical"]
        log_analyzer = LogAnalyzer(log_files, error_patterns)
        log_analyzer.analyze_logs()
    ```

3. Save and close the file. The Python Log Analyzer is now ready to analyze your logs for the specified error patterns.

# LogAnalyzer - Usage Guide

The `LogAnalyzer` is a Python utility that uses AI to analyze system logs and detect anomalies. It also summarizes errors and patterns in real-time.

## 1. Basic Usage Examples

First, you will have to import the `LogAnalyzer` class from the module. Below is an example of how to use the `LogAnalyzer`:

```python
from log_analyzer import LogAnalyzer

# Define the log files and error patterns
log_files = ['logfile1.log', 'logfile2.log']
error_patterns = ['Error 404', 'Error 500']

# Create an instance of LogAnalyzer
analyzer = LogAnalyzer(log_files, error_patterns)

# Analyze the logs
analyzer.analyze_logs()

# Generate the report
analyzer.generate_report()
```

## 2. Common Use Cases

- **Detecting and summarizing errors in log files**: The primary use case of the `LogAnalyzer` is to analyze log files for specific error patterns and summarize them. This can be done by passing the log files and error patterns during object creation and calling the `analyze_logs` method.
  
- **Generating a daily report of errors**: `LogAnalyzer` can also generate a daily report of all the anomalies and errors detected. This can be done by calling the `generate_report` method.

## 3. Command-line Arguments or Parameters

The `LogAnalyzer` class accepts two parameters in its constructor:

- **log_files**: A list of log files to be analyzed. These should be in the form of strings with the full file path.
- **error_patterns**: A list of error patterns to look for in the logs.

## 4. Expected Output Examples

When the `analyze_logs` method is called, it will analyze the log files and store the summary of detected errors in the `error_summary` attribute. This attribute is a dictionary where the keys are the error patterns and the values are the counts of their occurrences.

```python
analyzer.analyze_logs()
print(analyzer.error_summary)
```
Output:
```python
{'Error 404': 15, 'Error 500': 7}
```

When the `generate_report` method is called, it will generate a daily report summarizing all the anomalies and errors detected.

```python
analyzer.generate_report()
```
Output:
```plaintext
Daily Error Report
------------------
Error 404: 15 occurrences
Error 500: 7 occurrences
```

## 5. Advanced Usage Scenarios

- **Analyzing multiple log files**: You can pass multiple log files to the `LogAnalyzer` to be analyzed at once.

```python
log_files = ['logfile1.log', 'logfile2.log', 'logfile3.log']
analyzer = LogAnalyzer(log_files, error_patterns)
```

- **Detecting multiple error patterns**: You can pass multiple error patterns to the `LogAnalyzer` to detect all of them.

```python
error_patterns = ['Error 404', 'Error 500', 'Error 503']
analyzer = LogAnalyzer(log_files, error_patterns)
```

- **Scheduled log analysis**: You can use Python's `threading` and `time` modules to schedule the log analysis at certain intervals.

```python
def scheduled_analysis():
    analyzer = LogAnalyzer(log_files, error_patterns)
    while True:
        analyzer.analyze_logs()
        time.sleep(86400)  # delay for 1 day

analysis_thread = threading.Thread(target=scheduled_analysis)
analysis_thread.start()
```

This will run the log analysis every day on a separate thread.

# LogAnalyzer API Documentation

## Class: LogAnalyzer

A class used to analyze system logs and detect anomalies.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| log_files | list | A list of log files to be analyzed. |
| error_patterns | list | A list of error patterns to be detected. |
| error_summary | dict | A dictionary to store the summary of detected errors. |

### Methods

#### `__init__(self, log_files: List[str], error_patterns: List[str])`

Constructs all the necessary attributes for the `LogAnalyzer` object.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| log_files | list | A list of log files to be analyzed. |
| error_patterns | list | A list of error patterns to be detected. |

**Returns:**

This method does not return a value.

**Example:**

```python
log_files = ['/path/to/log1', '/path/to/log2']
error_patterns = ['ERROR', 'CRITICAL']
analyzer = LogAnalyzer(log_files, error_patterns)
```

#### `analyze_logs(self)`

Analyzes the log files and detects anomalies.

**Parameters:**

This method does not accept any parameters.

**Returns:**

This method does not return a value but populates the `error_summary` dictionary.

**Example:**

```python
analyzer.analyze_logs()
```

#### `generate_report(self)`

Generates a daily report summarizing all the anomalies and errors detected.

**Parameters:**

This method does not accept any parameters.

**Returns:**

This method does not return a value.

**Example:**

```python
analyzer.generate_report()
```

## Best Practices

- Use absolute paths when specifying the log_files to be analyzed to avoid any confusion.
- The error_patterns should be designed in a way that they uniquely identify the errors or anomalies you are interested in.
- Run the `analyze_logs` method at regular intervals (for example, daily or hourly), depending on the volume of logs your system generates.
- Run the `generate_report` method once a day to generate a daily report of the anomalies detected.

## Common Patterns

- The `LogAnalyzer` class can be used in a multi-threaded environment where each thread is responsible for analyzing a different set of log files.
- The `error_summary` dictionary can be used to store the count of each error pattern detected in the logs. This can provide a quick overview of the types of errors occurring in your system.

## Error Handling

- Make sure the log files specified in the `log_files` list exist and can be read. If a file does not exist or cannot be read, an `IOError` will be raised.
- If an invalid pattern is specified in the `error_patterns` list, a `re.error` will be raised. Make sure all the patterns are valid regular expressions.

## ⚙️ Configuration
Configuration options for customizing the application's behavior.

## 🔍 Troubleshooting
Common issues and their solutions.

## 🤝 Contributing
Guidelines for contributing to the project.

## 📄 License
This project is licensed under the MIT License.

## API Documentation

### Endpoints

#### `GET /api/resource`

Returns a list of resources.

**Parameters:**

- `limit` (optional): Maximum number of resources to return

**Response:**

```json
{
  "resources": [
    {
      "id": 1,
      "name": "Resource 1"
    }
  ]
}
```
