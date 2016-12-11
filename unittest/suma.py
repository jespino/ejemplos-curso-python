import unittest

class SumaTestCase(unittest.TestCase):
    def test_suma_good(self):
        result = 2 + 2
        self.assertEqual(result, 4)

    def test_suma_bad(self):
        result = 2 + 2
        self.assertEqual(result, 5)

if __name__ == "__main__":
    unittest.main()
