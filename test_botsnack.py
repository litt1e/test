import unittest
from mock import MagicMock
from modules import botsnack
import random

class TestBotsnack(unittest.TestCase):
    self.phenny = MagicMock()
    self.input = MagicMock()
    self.current_hunger = random.randint(1, 100)

    def test_increase_hunger(self):
        return botsnack.increase_hunger(self.current_hunger, 10)

    def test_decrease_hunger(self):
        for a in [40, 55]:
            self.current_hunger = a
            yield botsnack.decrease_hunger(self.current_hunger, 100 - self.current_hunger)

    def test_botsnack(self):
        return botsnack.botsnack(self.phenny, self.input)

    def test_botslap(self):
        return botsnack.botslap(self.phenny, self.input)



