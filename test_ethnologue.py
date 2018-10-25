import unittest
from modules import ethnologue
from mock import MagicMock

class TestEthnologue(unittest.TestCase):
    def setUp(self):
        self.input = MagicMock()
        self.phenny = MagicMock()

    def test_shorten_num(self):
        l = [1000, 100000, 1000000, 992415]
        for a in l:
            ethnologue.shorten_num(a)

    def test_scrape_ethnologue_codes(self):
        ethnologue.scrape_ethnologue_codes(self.phenny)

    def test_write_ethnologue_codes(self):
        a.MagicMock.return_value = raw.admin
        if ethnologue(self.phenny) == False:
            print('it\'s work')
        else:
            print('no')
        if ehnologue(self.phenny, a) == True:
            print('it\'s work')
        else:
            print('no')

    def test_parse_num_speakers(self):
        l = ['23, 324, 432, no known l1 speakers', '2342, 23, 22, l2 ethnic population',
             '2342, 23 , 22']
        for a in l:
            ethnologue.parse_num_speakers(a)

    def test_ethnologue(self):
        ethnologue.ethnologue(self.phenny, self.input)