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
        pass

    def score_three_of_a_kind(self, hand):
        return self._score_set(hand, 3)

    def score_four_of_a_kind(self, hand):
        return self._score_set(hand, 4)

    def score_yatzy(self, hand):
        if self._score_set(hand, 5):
            return 50
        return 0
