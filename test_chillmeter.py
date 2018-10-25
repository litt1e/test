from modules import chillmeter
import unittest
from mock import MagicMock

class TestChillmeter(unittest.TestCase):
    def setUp(self):
        self.input = MagicMock()
        self.phenny = MagicMock()

    def test_measure(self):
        return chillmeter.measure(self.phenny, self.input)

    def test_chill(self):
        return chillmeter.chill(self.phenny, self.input)