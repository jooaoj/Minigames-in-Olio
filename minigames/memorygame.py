"""
Title:          memorygame.py
Author(s):      Jooa Jaakkola
Description:    Memorygame()-class for mini-games
"""
from random import choice


class Memorygame:
    def __init__(self):
        """
        Mini-game -specific attributes initialised:
        """
        self.title = " -¤- The Most Malicious Memory-game -¤- "
        self.board = [" # "] * 16
        self.marks = ('%', '@', '¤')  # Tuple, because should be immutable.

        self.pair = choice(self.marks)
        self.pairs = ""

    def move(self, place):
        """
        Makes user able to pick a place from matrix in the console:
        """
        self.board[place] = " W "
        return True

    def isGameOver(self):
        # "PSEUDOCODE" ROUGH SKETCH:
        # if win_condition
        #   return 1
        # elif no win_condition
        #   return 0
        # else  # Lose if too many failed guesses.
        #   return 2
        return 1  # 0 => Continue game | 1 => Win | 2 => Lose

    def reset(self):
        self.board = [" # "] * 16
