import unittest

from app import LogEntry


class LogEntryTestCase(unittest.TestCase):
    def test_level_name(self):
        log = LogEntry("", 1, "Test")
        self.assertEqual(log.level_name(), "ERROR")
        log = LogEntry("", 2, "Test")
        self.assertEqual(log.level_name(), "WARN")
        log = LogEntry("", 3, "Test")
        self.assertEqual(log.level_name(), "INFO")
        log = LogEntry("", 4, "Test")
        self.assertEqual(log.level_name(), "INFO")

if __name__ == "__main__":
    unittest.main()
