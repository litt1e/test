import unittest
from modules import foodforus
from mock import MagicMock

class TestFoodforus(unittest.TestCase):
    def setUp(self):
        self.phenny = MagicMock()
        self.input = MagicMock()

    def test_food(self):
        foodforus.food(self.phenny, self.input)

    def test_foodvote(self):
        self.input.group(2).return_value = None
        self.input.group(3).return_value = None
        foodforus.foodvote(self.phenny, self.input)
        self.input.group(3).return_value = True
        foodforus.foodvote(self.phenny, self.input)

    def test_pickfood(self):
        self.input.group(2).return_value = 'testKey'
        foodforus.pickfood(self.phenny, self.input)
