import unittest

class RestaTestCase(unittest.TestCase):
    def test_resta_good(self):
        result = 2 - 2
        self.assertEqual(result, 0)

    @unittest.expectedFailure
    def test_resta_bad(self):
        result = 2 - 2
        self.assertEqual(result, 1)

if __name__ == "__main__":
    unittest.main()
