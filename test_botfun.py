import unittest
from modules import botfun
from mock import MagicMock

class TestBotfun(unittest.TestCase):
    nick = 'test'
    def setUp(self):
        self.phenny = MagicMock()
        self.input = MagicMock()

    def test_botfight(self):
        return botfun.botfight(self.phenny, self.input)

    def test_bothug(self):
        return botfun.bothug(self.phenny, self.input)



