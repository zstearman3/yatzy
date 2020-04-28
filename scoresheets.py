class YatzyScoresheet:

    def score_ones(self, hand):
        return sum(hand.ones)

    def score_twos(self, hand):
        return sum(hand.twos)

    def score_threes(self, hand):
        return sum(hand.threes)

    def score_fours(self, hand):
        return sum(hand.fours)

    def score_fives(self, hand):
        return sum(hand.fives)

    def score_sixes(self, hand):
        return sum(hand.sixes)

    def _score_set(self, hand, set_size):
        scores = [0]
        for worth, count in hand._sets.items():
            if count == set_size:
                scores.append(worth*set_size)
        return max(scores)

    def score_one_pair(self, hand):
        return self._score_set(hand, 2)

    def score_two_pairs(self, hand):
        scores = []
        for worth, count in hand._sets.items():
            if count == 2:
                scores.append(worth*2)
        if len(scores) == 2:
            return sum(scores)
        else:
            return 0

    def score_three_of_a_kind(self, hand):
        return self._score_set(hand, 3)

    def score_full_house(self, hand):
        scores = []
        pair = False
        three_of_a_kind = False
        for worth, count in hand._sets.items():
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

    def score_four_of_a_kind(self, hand):
        return self._score_set(hand, 4)

    def score_chance(self, hand):
        return sum(hand)

    def score_small_straight(self, hand):
        if all([hand._sets[1] >= 1, hand._sets[2] >= 1, hand._sets[3] >=1,
                hand._sets[4] >= 1]) or all([hand._sets[2] >= 1, hand._sets[3] >= 1,
                hand._sets[4] >=1, hand._sets[5] >=1]) or all([hand._sets[3] >= 1,
                hand._sets[4] >= 1, hand._sets[5] >=1, hand._sets[6] >=1]):
            return 15

    def score_large_straight(self, hand):
        if all([hand._sets[2] == 1, hand._sets[3] == 1, hand._sets[4] == 1, hand._sets[5] == 1,
                hand._sets[6] == 1]) or all([hand._sets[1] == 1, hand._sets[2] == 1,
                hand._sets[3] == 1, hand._sets[4] == 1, hand._sets[5] == 1]):
            return 20

    def score_yatzy(self, hand):
        if self._score_set(hand, 5):
            return 50
        return 0

    def score_max(self, limit=None):
        scores = {
            'ones': self.score_ones(),
            'twos': self.score_twos(),
            'threes':self.score_threes(),
            'fours': self.score_fours(),
            'fives': self.score_fives(),
            'sixes': self.score_sixes(),
            'one_pair': self.score_one_pair(),
            'two_pairs': self.score_two_pairs(),
            'three_of_a_kind': self.score_three_of_a_kind(),
            'four_of_a_kind': self.score_four_of_a_kind(),
            'full_house': self.score_full_house(),
            'small_straight': self.score_small_straight(),
            'large_straight': self.score_large_straight(),
            'chance': self.score_chance(),
            'yatzy': self.score_yatzy()
        }
        if limit:
            for key in scores.copy():
                if key not in limit:
                    del scores[key]
        return max(scores, key=scores.get)

        @property
        def left_to_reroll(self, hand):
            return any([die.can_be_rerolled for die in hand])

class Category:
    def __init__(self, name, display, key, score=None):
        self.name = name
        self.display = display
        self.key = key
        self.score = score

    def __str__(self):
        return self.display

    def __add__(self, other):
        return self.score + other

    def __radd__(self, other):
        return self.score + other
