"""
Title:          memorygame.py
Author(s):      Paavo Makela, Jooa Jaakkola, Mio Saari, Nea Virtanen & Roope Kakko
Description:    Memorygame()-class inheriting prototype Boardgame()
"""
# Python built-ins:
from random import choice, shuffle

# From PATH:
from minigames.boardgame import Boardgame
from buttonsBlock import ButtonsBlock


class Memorygame(Boardgame):

    def __init__(self):
        super().__init__()
        self.title = "Memorygame"

        self.pair = []
        self.pairs = [self.bgSymbol for _ in range(self.size * self.size)]

        self.reset()

    def move(self, place: int) -> bool:
        if self.board['visible'][place] != self.bgSymbol or place > len(self.board['visible']):
            return False

        # If there is already 2 pairs
        if len(self.pair) == 2:
            # If pair does not match clear those slots in board
            if self.pair[0][1] != self.pair[1][1]:
                self.board['visible'][self.pair[0][0]] = self.bgSymbol
                self.board['visible'][self.pair[1][0]] = self.bgSymbol

            # Clear pairs
            self.pair = []

        self.board['visible'][place] = self.pairs[place]
        self.pair.append((place, self.pairs[place]))

        return True

    def isGameOver(self) -> int:
        # 0 = game is still going
        # 1 = player wins
        return 1 if self.board['visible'] == self.pairs else 0

    def reset(self):
        # Copy all possible marks into a list
        symbolPool = list(self.symbols)

        for i in range(0, len(self.pairs), 2):
            # Choose a symbol
            symbol = choice(symbolPool)
            # Remove from symbol pool so same symbol can't
            # come up twice
            symbolPool.remove(symbol)

            # Add a pair of marks
            self.pairs[i] = symbol
            self.pairs[i + 1] = symbol

        # Shuffles the pairs list so marks aren't in order
        shuffle(self.pairs)

        # Empty board
        super().reset()
