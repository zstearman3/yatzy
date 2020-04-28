import unittest

import dice

class DiceTests(unittest.TestCase):
    def test_die(self):
        die = dice.Die()
        self.assertIn(int(die), range(1, 7))

    def test_die_value(self):
        die = dice.Die(value=8)
        self.assertEqual(int(die), 8)

    def test_d6(self):
        die = dice.D6()
        self.assertEqual(die.sides, 6)

    def test_d6_value(self):
        die = dice.D6()
        self.assertLessEqual(int(die), 6)
