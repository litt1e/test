import unittest
from modules import choose
from mock import MagicMock

class TestChoose(unittest.TestCase):
    def setUp(self):
        self.phenny = MagicMock()
        self.input = MagicMock()

    def test_choose(self):
        origterm = self.input.group.return_value = 1
        choose.choose(self.phenny, self.input)
        self.assertTrue(origterm)