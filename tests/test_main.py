import unittest
from main import LogAnalyzer

class TestLogAnalyzer(unittest.TestCase):
    def setUp(self):
        self.log_analyzer = LogAnalyzer("test.log")

    def test_read_logs(self):
        logs = self.log_analyzer.read_logs()
        self.assertIsInstance(logs, list)

    def test_analyze_logs(self):
        logs = ["ERROR This is an error", "WARNING This is a warning"]
        anomalies = self.log_analyzer.analyze_logs(logs)
        self.assertEqual(len(anomalies["errors"]), 1)
        self.assertEqual(len(anomalies["warnings"]), 1)

if __name__ == "__main__":
    unittest.main()