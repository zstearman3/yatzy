from dice import D6
import time

class Hand(list):
    def __init__(self, size=0, die_class=D6):
        super().__init__()

        for _ in range(size):
            self.append(die_class())

        self.sort()

    def _by_value(self, value):
        dice = []
        for die in self:
            if die == value:
                dice.append(die)
        return dice


class YatzyHand(Hand):
    def __init__(self):
        super().__init__(size=5, die_class=D6)

        self.scorers = {
            'ones': self.score_ones,
            'twos': self.score_twos,
            'threes': self.score_threes,
            'fours': self.score_fours,
            'fives': self.score_fives,
            'sixes': self.score_sixes,
            'one_pair': self.score_one_pair,
            'two_pairs': self.score_two_pairs,
            'three_of_a_kind': self.score_three_of_a_kind,
            'four_of_a_kind': self.score_four_of_a_kind,
            'full_house': self.score_full_house,
            'small_straight': self.score_small_straight,
            'large_straight': self.score_large_straight,
            'chance': self.score_chance,
            'yatzy': self.score_yatzy
        }

    @property
    def ones(self):
        return self._by_value(1)

    @property
    def twos(self):
        return self._by_value(2)

    @property
    def threes(self):
        return self._by_value(3)

    @property
    def fours(self):
        return self._by_value(4)

    @property
    def fives(self):
        return self._by_value(5)

    @property
    def sixes(self):
        return self._by_value(6)

    @property
    def _sets(self):
        return{
            1: len(self.ones),
            2: len(self.twos),
            3: len(self.threes),
            4: len(self.fours),
            5: len(self.fives),
            6: len(self.sixes)
        }

    def display(self, width=0, show_key=False):
        die_lines = []
        for die in self:
            die_lines.append(die.display.split('\n'))
        for i in range(5):
            for die in die_lines:
                print('{0:^{1}}'.format(die[i], width//5), end='')
            print('')
            if show_key:
                for num in range(1, 6):
                    if self[num-1].can_be_rerolled:
                        print('{0:^{1}}'.format('', width//5), end='')
                print('')

    def score(self, what):
        return self.scorers[what]()

    @property
    def left_to_reroll(self):
        return any([die.can_be_rerolled for die in self])

    def score_ones(self):
        return sum(self.ones)

    def score_twos(self):
        return sum(self.twos)

    def score_threes(self):
        return sum(self.threes)

    def score_fours(self):
        return sum(self.fours)

    def score_fives(self):
        return sum(self.fives)

    def score_sixes(self):
        return sum(self.sixes)

    def _score_set(self, set_size):
        scores = [0]
        for worth, count in self._sets.items():
            if count == set_size:
                scores.append(worth*set_size)
        return max(scores)

    def score_one_pair(self):
        return self._score_set(2)

    def score_two_pairs(self):
        scores = []
        for worth, count in self._sets.items():
            if count == 2:
                scores.append(worth*2)
        if len(scores) == 2:
            return sum(scores)
        else:
            return 0

    def score_three_of_a_kind(self):
        return self._score_set(3)

    def score_full_house(self):
        scores = []
        pair = False
        three_of_a_kind = False
        for worth, count in self._sets.items():
            if count == 2:
                scores.append(worth*2)
                pair = True
            elif count == 3:
                scores.append(worth*3)
                three_of_a_kind = True
        if pair and three_of_a_kind:
            return sum(scores)
        else:
            return 0

    def score_four_of_a_kind(self):
        return self._score_set(4)

    def score_chance(self):
        return sum(self)

    def score_small_straight(self):
        if all([self._sets[1] >= 1, self._sets[2] >= 1, self._sets[3] >=1,
                self._sets[4] >= 1]) or all([self._sets[2] >= 1, self._sets[3] >= 1,
                self._sets[4] >=1, self._sets[5] >=1]) or all([self._sets[3] >= 1,
                self._sets[4] >= 1, self._sets[5] >=1, self._sets[6] >=1]):
            return 15

    def score_large_straight(self):
        if all([self._sets[2] == 1, self._sets[3] == 1, self._sets[4] == 1, self._sets[5] == 1,
                self._sets[6] == 1]) or all([self._sets[1] == 1, self._sets[2] == 1,
                self._sets[3] == 1, self._sets[4] == 1, self._sets[5] == 1]):
            return 20

    def score_yatzy(self):
        if self._score_set(5):
            return 50
        return 0

    def score_max(self, limit=None):
        scores = {
            '1': self.score_ones(),
            '2': self.score_twos(),
            '3': self.score_threes(),
            '4': self.score_fours(),
            '5': self.score_fives(),
            '6': self.score_sixes(),
            'O': self.score_one_pair(),
            'T': self.score_two_pairs(),
            'K': self.score_three_of_a_kind(),
            'F': self.score_four_of_a_kind(),
            'H': self.score_full_house(),
            'S': self.score_small_straight(),
            'L': self.score_large_straight(),
            'C': self.score_chance(),
            'Y': self.score_yatzy()
        }
        if limit:
            open_categories = []
            for category in limit:
                open_categories.append(category.key)
            for key in scores.copy():
                if key not in open_categories:
                    del scores[key]
        return max(scores, key=scores.get)
