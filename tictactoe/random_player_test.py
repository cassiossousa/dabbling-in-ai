import unittest
from random_player import *
from board import *

empty_grid = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

partially_filled_grid = [
    ["O", "X", "O"],
    ["X", "O", "X"],
    [None, None, None]
]


# Basic tests for a random player.


class RandomPlayerTests(unittest.TestCase):
    def test_empty_grid(self):
        empty_board = Board()
        empty_board.create_board_from_grid(empty_grid)
        rand_player = RandomPlayer(1, empty_board, "O")
        play = rand_player.strategy()
        assert 0 <= play <= 8

    def test_partially_filled_grid(self):
        partially_filled_board = Board()
        partially_filled_board.create_board_from_grid(partially_filled_grid)
        rand_player = RandomPlayer(1, partially_filled_board, "O")
        play = rand_player.strategy()
        assert 6 <= play <= 8


def main():
    unittest.main()


if __name__ == '__main__':
    main()
