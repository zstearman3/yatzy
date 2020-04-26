import random
from scoresheets import YatzyScoresheet

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

class PlayerScoresheet():
    pass
