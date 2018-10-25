import unittest
from modules import ping
from mock import MagicMock

class TestPing(unittest.TestCase):
    def setUp(self):
        self.phenny = MagicMock()
        self.input = MagicMock()

    def test_getGuset(self):
        self.input.return_value = input.admin
        ping.getGuests(self.phenny, self.input)
        self.input.return_value = False
        ping.getGuests(self.phenny, self.input)

    def test_hello(self):
        self.input.return_value = input.nick
        ping.hello(self.phenny, self.input)

    def test_interjection(self):
        ping.interjection(self.phenny, self.input)
