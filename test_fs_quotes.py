import unittest
from modules import fs_quotes
from mock import MagicMock

class TestFsQuotes:
    def setUp(self):
        self.phenny = MagicMock()
        self.input = MagicMock()

    def test_infromation(self):
        self.input.group(1).return_value = 'testtopic'
        fs_quotes.information(self.phenny, self.input)
        self.input.group(1).return_value = 'particles'
        fs_quotes.information(self.phenny, self.input)

    def test_randquote_fetcher(self):
        fs_quotes.randquote(self.phenny, 'topic', 'user')

