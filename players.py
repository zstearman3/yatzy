import random
from hands import YatzyHand
from scoresheets import YatzyScoresheet
from scoresheets import Category
import time

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
        self.hand = YatzyHand()
        return

    @property
    def score(self):
        return self.scoresheet.score

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

    def play_round(self):
        best_move = self.hand.score_max(self.scoresheet.open_categories)
        score = self.hand.score(best_move[1])
        print('-' * 10)
        print(f'{self.name} plays {best_move[1]} for {score} points.')
        print('-' * 10)
        time.sleep(2.5)
        self.scoresheet.score_category(best_move[0], score)
        return

class PlayerScoresheet():
    def __init__(self):
        self.categories = (
            Category('ones', 'Ones', '1'),
            Category('twos', 'Twos', '2'),
            Category('threes', 'Threes', '3'),
            Category('fours', 'Fours', '4'),
            Category('fives', 'Fives', '5'),
            Category('sixes', 'Sixes', '6'),
            Category('one_pair', 'One Pair', 'O'),
            Category('two_pairs', 'Two Pairs', 'T'),
            Category('three_of_a_kind', 'Three of a Kind', 'K'),
            Category('four_of_a_kind', 'Four of a Kind', 'F'),
            Category('small_straight', 'Small Straight', 'S'),
            Category('large_straight', 'Large Straight', 'L'),
            Category('full_house', 'Full House', 'H'),
            Category('chance', 'Chance', 'C'),
            Category('yatzy', 'Yatzy', 'Y')
        )

    def __getitem__(self, item):
        try:
            return [category for category in self.categories if category.name == item][0]
        except IndexError:
            raise KeyError

    def get_by_key(self, key):
        try:
            return [category for category in self.categories if category.key == key][0]
        except IndexError:
            raise KeyError

    def display(self, width):
        for index, category in enumerate(self.open_categories, start=1):
            print("{0:^{1}}".format(
                '{} [{}]'.format(category.display, category.key),
                width//3
            ), end='\t')
            if not index % 3:
                print ('')
        print('')

    @property
    def score(self):
        return sum([score for score in self.categories if score.score is not None])

    @property
    def open_categories(self):
        categories = []
        for category in self.categories:
            if category.score is None:
                categories.append(category)
        return categories

    @property
    def open_keys(self):
        keys = []
        for category in self.categories:
            if category.score is None:
                keys.append(category.key)
        return keys

    def score_category(self, key, score):
        try:
            category = [category for category in self.categories if category.key == key][0]
        except IndexError:
            raise KeyError
        category.score = score
