import unittest

from tests.unit_test.testExample import TestStringMethods
from tests.unit_test.testSample import TestSample

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestStringMethods('test_default_widget_size'))
    suite.addTest(TestSample('TestSample'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())