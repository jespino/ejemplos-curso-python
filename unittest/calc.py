import unittest
import suma
import resta

def suite():
    calc_suite = unittest.TestSuite()
    calc_suite.addTest(suma.SumaTestCase('test_suma_good'))
    calc_suite.addTest(suma.SumaTestCase('test_suma_bad'))
    calc_suite.addTest(resta.RestaTestCase('test_resta_good'))
    calc_suite.addTest(resta.RestaTestCase('test_resta_bad'))
    return calc_suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
