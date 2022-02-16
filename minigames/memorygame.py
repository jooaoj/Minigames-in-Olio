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
        self.marks = (' % ', ' @ ', ' ¤ ', ' * ', ' £ ')  # Tuple, because should be immutable.
        self.pair = [choice(self.marks), choice(self.marks)]
        # Maybe generate pair(s) into board with lambda?
        self.board = [" _ "] * 16
        self.pairs = [self.pair[0], self.pair[1]] * 16

        self.exampleBoard = [f" {self.pair[0] or self.pair[1]} "] * 16

    def move(self, place):
        """
        Makes user able to pick a place from matrix in the console:
        TESTing : generate exampleBoard outside real board and compare them.
                  HOW TO GET OG. BOARD THE "MARKS"-VALUES?
        """
        #print(self.pair)  # For clarification in testing...
        coordinates = self.board[place] # => This returns "A1, B3... etc."
        if coordinates == self.exampleBoard[coordinates]:
            print("YES")
            return True
        else:
            print("NOh")
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
