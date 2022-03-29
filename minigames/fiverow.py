"""
Title:              fiverow.py
Author:             Paavo Makela, Jooa Jaakkola, Mio Saari, Nea Virtanen & Roope Kakko
Description:        FiveRow Lab 2 - added serialization.
"""
import random
import json

# From PATH:
from minigames.boardgame import Boardgame


class FiveRow(Boardgame):

    def __init__(self):
        super().__init__()
        self.title = "Five-in-a-Row"
        self.players = ('X', 'O')

    # ~~ #

    def move(self, place):
        """
        Removing available moves from the bot (and player).
        """

        def remove(lst):
            for move in lst:
                moves.remove(move) if move in moves else None

        if self.board[place] != "   ":
            return False

        self.board[place] = " X "
        result = self.isGameOver()
        print(result, 'result')
        if result != 1:

            # Randomly find an available place close to user's move, but
            # prevent jumping to the opposite side of the board so the
            # move looks at least slightly reasonable.
            while self.board[place] != "   ":
                moves = [1, -1, 11, -11, 12, -12, 13, -13]
                if place % 12 == 0:
                    remove([-1, 11, -13])
                elif place % 12 == 11:
                    remove([1, -11, 13])
                if place < 12:
                    remove([-11, -12, -13])
                elif place > 12 * 11:
                    remove([11, 12, 13])

                place += random.choice(moves)

            self.board[place] = " O "

        return True

    def isGameOver(self):
        """
        Safeguarding if several rows of fives
        are found on the same move, or win condition otherwise met:
        """
        def foundFive():
            n = 1 if mark == " X " else 2
            if status < 3 and status != n:
                return status + n
            else:
                return status

        free = False
        status = 0

        for place in range(0, 12 ** 2):
            if self.board[place] == "   ":
                free = True
                continue

            mark = self.board[place]

            # Horizontal
            if place % 12 <= 12 - 5:
                for i in range(1, 5):
                    if self.board[place + i] != mark:
                        break
                else:
                    status = foundFive()
                    continue

            # Vertical
            if place < 12 ** 2 - 4 * 12:
                for i in range(1, 5):
                    if self.board[place + 12 * i] != mark:
                        break
                else:
                    status = foundFive()
                    continue

            # Diagonal right
            if place % 12 <= 12 - 5 and place < 12 ** 2 - 4 * 12:
                for i in range(1, 5):
                    if self.board[place + i + 12 * i] != mark:
                        break
                else:
                    status = foundFive()
                    continue

            # Diagonal left
            if place % 12 >= 4 and place < 12 ** 2 - 4 * 12:
                for i in range(1, 5):
                    if self.board[place - i + 12 * i] != mark:
                        break
                else:
                    status = foundFive()
                    continue

        # Win can happen on the last possible move and that shouldn't
        # be treated as a tie.
        if not free and status == 0:
            status = 3

        return status

    def reset(self):
        self.board = 12 ** 2 * ["   "]
