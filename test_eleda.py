import unittest
from modules import eleda
from mock import MagicMock

class TestEleda(unittest.TestCase):
    def setUp(self):
        self.phenny = MagicMock()
        self.input = MagicMock()

    def test_follow(self):
        l = ['Nick name en-es', 'test test test']
        for a in l:
            eleda.follow(self.phenny, a)

    def test_unfollow(self):
        eleda.unfollow(self.phenny, self.input)

    def test_following(self):
        eleda.following(self.phenny, self.input)

    def test_checkMessages(self):
        self.input.return_value = '.command'
        eleda.checkMessages(self.phenny, self.input)