"""
Title:          memorygame.py
Author(s):      Paavo Makela, Jooa Jaakkola, Mio Saari, Nea Virtanen & Roope Kakko
Description:    Memorygame()-class for mini-games
"""
# Python built-ins:
from random import choice, shuffle

# From PATH:
from boardgame import Boardgame


class Memorygame(Boardgame):

    title = "Memogame"

    def __init__(self):
        super(Memorygame, self).__init__()

        # List full of white spaces
        # Pairs holds values hidden from player.
        self.pairs = [" * " for _ in range(self.size)]
        self.pair = []
    
        # List full of white spaces
        self.board = [" * " for _ in range(self.size)]

    # ~~ #

    def move(self) -> bool:
        self.place =

        if self.board[place] != " * " or place > len(self.board):
            # Invalid move
            return False

        # If there is already 2 pairs
        if len(self.pair) == 2:
            # If pair does not match clear those slots in board
            if self.pair[0][1] != self.pair[1][1]:
                self.board[self.pair[0][0]] = " * "
                self.board[self.pair[1][0]] = " * "

            # Clear pairs
            self.pair = []

        self.board[place] = self.pairs[place]
        self.pair.append((place, self.pairs[place]))

        return True