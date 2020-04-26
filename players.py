import random
from scoresheets import YatzyScoresheet

BOT_NAMES = [
    'Jon Snow',
    'Daenerys Targaryen',
    'Arya Stark',
    'Sansa Stark',
    'Khal Drogo',
    'Gregor Clegane',
    'Tyrion Lannister',
    'Cersei Lannister',
    'Ramsay Bolton',
    'Theon Grejoy',
    'Brienne of Tarth'
]

class Player():
    def __init__(self, order):
        self.order = order
        self.scoresheet = PlayerScoresheet()
        self.hand = None

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, str(self))

    def roll(self):
        self.hand = dice.Hand()
        return

    def score(self):
        return self.scoresheet

class HumanPlayer(Player):
    def __init__(self, order, name=None):
        super().__init__(order)
        self.name = name

    def __str__(self):
        return self.name

class BotPlayer(Player):
    def __init__(self, order):
        super().__init__(order)
        self.name = random.choice(BOT_NAMES)

    def __str__(self):
        return self.name

class PlayerScoresheet():
    pass
