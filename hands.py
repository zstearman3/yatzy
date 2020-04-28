from dice import D6

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
