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

class D6(Die):
    def __init__(self, value=0):
        super().__init__(sides=6, value=value)
