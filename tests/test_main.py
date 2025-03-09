import unittest
from log_monitor import LogMonitor

class TestLogMonitor(unittest.TestCase):
    def setUp(self):
        self.log_monitor = LogMonitor(["/var/log"], 0.5)

    def test_process_log(self):
        # Test that process_log updates error_summary
        self.log_monitor.process_log("/var/log/test.log")
        self.assertTrue("/var/log/test.log" in self.log_monitor.get_summary())

    def test_get_summary(self):
        # Test that get_summary returns a dictionary
        self.assertIsInstance(self.log_monitor.get_summary(), dict)

    def test_get_alerts(self):
        # Test that get_alerts returns a list
        self.assertIsInstance(self.log_monitor.get_alerts(), list)

if __name__ == '__main__':
    unittest.main()