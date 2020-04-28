import random

class Die:
    def __init__(self, sides=6, value=0):
        if not sides >=2:
            raise ValueError("Must have at least 2 sides")
        if not isinstance(sides, int):
            raise ValueError("Sides must be a whole number")
        if not isinstance(value, int):
            raise ValueError("Value must be a whole number")
        self.value = value or random.randint(1, sides)
        self.sides = sides

    def __int__(self):
        return self.value

    def __eq__(self, other):
        return int(self) == other

    def __ne__(self, other):
        return not int(self) == other

    def __gt__(self, other):
        return int(self) > other

    def __lt__(self, other):
        return int(self) < other

    def __ge__(self, other):
        return int(self) >= other

    def __le__(self, other):
        return int(self) <= other

    def __add__(self, other):
        return int(self) + other

    def __radd__(self, other):
        return int(self) + other

    def __repr__(self):
        return str(self.value)

class D6(Die):
    MAX_ROLLS = 3

    template = """
    | {} {} {} |
    | {} {} {} |
    | {} {} {} |
    """

    pips = {
        1: [' ', ' ', ' ',
            ' ', '*', ' ',
            ' ', ' ', ' '],
        2: ['*', ' ', ' ',
            ' ', ' ', ' ',
            ' ', ' ', '*'],
        3: ['*', ' ', ' ',
            ' ', '*', ' ',
            ' ', ' ', '*'],
        4: ['*', ' ', '*',
            ' ', ' ', ' ',
            '*', ' ', '*'],
        5: ['*', ' ', '*',
            ' ', '*', ' ',
            '*', ' ', '*'],
        6: ['*', ' ', '*',
            '*', ' ', '*',
            '*', ' ', '*'],
    }

    def __init__(self, value=0):
        super().__init__(sides=6, value=value)
        self.rolls = 1

    def reroll(self):
        if self.rolls == self.MAX_ROLLS:
            raise Exception('Can only roll a die 3 times')
        self.value = random.randint(1, 6)
        self.rolls += 1

    @property
    def can_be_rerolled(self):
        return self.rolls < self.MAX_ROLLS

    @property
    def display(self):
        return self.template.format(*self.pips[self.value])
