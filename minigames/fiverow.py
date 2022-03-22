"""
Title:              fiverow.py
Author:             Paavo Makela, Jooa Jaakkola, Mio Saari, Nea Virtanen & Roope Kakko
Description:        FiveRow Lab 2 - added serialization.
"""
import random

import random
import json


class FiveRow:
    # Class variable is one outside __init__
    filename = "fiverow.json"

    def __init__(self):
        self.title = "Five-in-a-Row"
        self.board = 12 ** 2 * ["   "]

    # board to test for tie
    # self.board = \
    # [' X ', ' O ',' X ',' X ',' O ',' X ',' O ',' O ',' O ',' X ',' X ',' X ',\
    # ' X ', ' X ',' O ',' X ',' X ',' O ',' X ',' X ',' X ',' O ',' O ',' X ',\
    # ' X ', ' X ',' X ',' X ',' O ',' O ',' X ',' O ',' X ',' X ',' O ',' O ',\
    # ' X ', ' X ',' O ',' X ',' O ',' X ',' O ',' O ',' X ',' X ',' X ',' X ',\
    # ' O ', ' X ',' O ',' O ',' O ',' X ',' O ',' X ',' O ',' X ',' X ',' X ',\
    # ' O ', ' O ',' X ',' X ',' X ',' O ',' X ',' O ',' X ',' O ',' X ',' O ',\
    # ' X ', ' O ',' O ',' X ',' X ',' O ',' X ',' O ',' X ',' O ',' X ',' O ',\
    # ' X ', ' X ',' X ',' O ',' O ',' O ',' O ',' X ',' X ',' X ',' O ',' X ',\
    # ' O ', ' O ',' X ',' O ',' X ',' O ',' O ',' X ',' O ',' X ',' X ',' X ',\
    # ' O ', ' X ',' X ',' X ',' O ',' X ',' O ',' X ',' X ',' O ',' X ',' X ',\
    # ' X ', ' O ',' X ',' X ',' O ',' O ',' X ',' O ',' X ',' X ',' X ',' X ',\
    # ' X ', ' X ',' O ',' X ',' O ',' O ',' O ',' O ',' X ',' X ',"   ","   "]

    @classmethod
    def serialize(cls, obj):
        """
        Serialize == save game state into external file (JSON)
        """
        with open(cls.filename, "w") as file:  # Open a file in write-mode and close it after use.
            json.dump(obj.__dict__, file)

    @classmethod
    def deserialize(cls):
        try:
            with open(cls.filename, "r") as file:  # Open a file in read-mode and close it after use.
                loaded = json.load(file)
                game = cls()
                # Copy loaded JSON to new cls-dict:
                for key in loaded.keys():
                    setattr(game, key, loaded[key])

        except FileNotFoundError:
            game = cls()

        return game  # a.k.a return "altered" game-argument back into main.py

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

    def reset(self):
        self.board = 12 ** 2 * ["   "]
