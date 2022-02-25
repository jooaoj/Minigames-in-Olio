"""
Title:          memorygame.py
Author(s):      Jooa Jaakkola
Description:    Memorygame()-class for mini-games
"""
from random import choice, shuffle


class Memorygame:
    def __init__(self):
        """
        Mini-game -specific attributes initialised:
        """
        self.title = " -¤- The Most Malicious Memory-game -¤- "
        self.marks = (0, 1, 2, 3, 4, 5, 6, 7)  # Tuple, because should be immutable.
        self.pairs = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]
        self.pair = []

        # Generates the game, so to speak...
        self.board = [" _ "] * 16
        shuffle(self.pairs)

    def move(self, place):
        """
        Makes user able to pick a place from matrix in the console:
        TESTing : generate exampleBoard outside real board and compare them.
                  HOW TO GET OG. BOARD THE "MARKS"-VALUES?
        """

        if 10 < 9:
            return True
        else:
            return False

    def isGameOver(self):
        """
        Checks whether all hashtags revealed or not:
        """
        if self.board == self.pairs:
            return 1
        elif self.board != self.pairs:
            return 0
        else:
            return 2

    def reset(self):
        self.board = [" # "] * 16
