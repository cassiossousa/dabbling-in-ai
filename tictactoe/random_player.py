from player import Player


class RandomPlayer(Player):
    def __init__(self, board, symbol):
        Player.__init__(self, board, symbol)

    def strategy(self):
        return self.random_play()
