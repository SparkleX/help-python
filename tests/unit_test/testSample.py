import unittest
from unittest.mock import MagicMock


class TestSample(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
