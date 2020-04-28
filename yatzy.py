import players

class Yatzy:
    def __init__(self, humans=0, bots=0):
        self.all_computer = (not humans and bots)
        self.humans = []
        self.bots = []

        self.current_round = 1
        self.scores = {}

        self.game_board_width = 90

        if humans and not self.all_computer:
            self.humans = self.get_humans(humans)

        if bots or self.all_computer:
            self.bots = self.get_bots(bots)

        if not humans and not bots:
            raise ValueError("Must provide either human or bot players")


def start_game():
    print("How many are playing? (Press ENTER for 0)")
    human_count = int(input("Human players? ") or 0)
    bot_count = int(input("Computer players? ") or 0)

    return human_count, bot_count

if __name__ == '__main__':
    try:
        humans, bots = start_game()
        game = Yatzy(humans=humans, bots=bots)
    except ValueError as err:
        print("No one's playing? OK")
    else:
        game.play()
