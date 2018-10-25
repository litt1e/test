import unittest
from modules import codepoints
from mock import MagicMock

class TestCodepoints(unittest.TestCase):
    def setUp(self):
        self.input = MagicMock()
        self.phenny = MagicMock()
        self.cp = MagicMock()
        self.name = MagicMock()

    def test_about(self):
        cp = self.cp.return_value = 2
        testname = self.name.return_value = 'test'
        u = 't'
        codepoints.about(u, cp, testname)

    def test_codepoint_simplt(self):
        test = self.input.return_value = 'abc'
        codepoints.codepoint_simple(test)

    def test_u(self):
        inp = self.input.return_value = bytes([list(range(0,100,10))])
        codepoints.u(self.phenny, inp)