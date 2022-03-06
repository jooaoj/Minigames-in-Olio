"""
Title:          memorygame.py
Author(s):      Jooa Jaakkola
Description:    Memorygame()-class for mini-games
"""
from random import choice, shuffle


class Memorygame:
    def __init__(self):
        # Size of game board
        size = 16
        self.title = "Memory game"
        # List full of white spaces. Pairs holds values hidden from player
        self.pairs = [" * " for _ in range(size)]
        self.pair = []
        # All small alphabets
        self.marks = tuple([" " + chr(asciiCharacter)+ " " for asciiCharacter in range(97, 123)])
        # List full of white spaces
        self.board = [" * " for _ in range(size)]
        # Reuse reset to initialize pairs
        self.reset()

    def move(self, place: int) -> bool:
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

    def isGameOver(self) -> int:
        # 0 = game is still going
        # 1 = player wins
        return 1 if self.board == self.pairs else 0

    def reset(self):
        # Copy all possible marks into a list
        markPool = list(self.marks)

        for i in range(0, len(self.pairs), 2):
            # Choose a mark
            mark = choice(markPool)
            # Remove from mark pool so same mark can't
            # come up twice
            markPool.remove(mark)

            # Add a pair of marks
            self.pairs[i] = mark
            self.pairs[i + 1] = mark

        # Shuffles the pairs list so marks aren't in order
        shuffle(self.pairs)

        # Empty board
        self.board = [" * " for _ in range(len(self.board))]