import unittest
import dice
import players

class PlayerTests(unittest.TestCase):
    def test_roll(self):
        player = players.Player(1)
        player.roll()
        self.assertEqual(len(player.hand), 5)

    def test_bot_name(self):
        bot = players.BotPlayer(1)
        self.assertTrue(bot.name is not None)
