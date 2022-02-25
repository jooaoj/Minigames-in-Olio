"""
Title:              main.py
Author:             Jooa Jaakkola (@benevolentimp)
Description:        A concise description of this file.
"""
import random


class FiveRow:
    def __init__(self):
        self.title = "Five-in-a-Row"
        self.board = 12 ** 2 * ["   "]

    # board to test for tie
    ##        self.board = \
    ##        [' X ', ' O ',' X ',' X ',' O ',' X ',' O ',' O ',' O ',' X ',' X ',' X ',\
    ##         ' X ', ' X ',' O ',' X ',' X ',' O ',' X ',' X ',' X ',' O ',' O ',' X ',\
    ##         ' X ', ' X ',' X ',' X ',' O ',' O ',' X ',' O ',' X ',' X ',' O ',' O ',\
    ##         ' X ', ' X ',' O ',' X ',' O ',' X ',' O ',' O ',' X ',' X ',' X ',' X ',\
    ##         ' O ', ' X ',' O ',' O ',' O ',' X ',' O ',' X ',' O ',' X ',' X ',' X ',\
    ##         ' O ', ' O ',' X ',' X ',' X ',' O ',' X ',' O ',' X ',' O ',' X ',' O ',\
    ##         ' X ', ' O ',' O ',' X ',' X ',' O ',' X ',' O ',' X ',' O ',' X ',' O ',\
    ##         ' X ', ' X ',' X ',' O ',' O ',' O ',' O ',' X ',' X ',' X ',' O ',' X ',\
    ##         ' O ', ' O ',' X ',' O ',' X ',' O ',' O ',' X ',' O ',' X ',' X ',' X ',\
    ##         ' O ', ' X ',' X ',' X ',' O ',' X ',' O ',' X ',' X ',' O ',' X ',' X ',\
    ##         ' X ', ' O ',' X ',' X ',' O ',' O ',' X ',' O ',' X ',' X ',' X ',' X ',\
    ##         ' X ', ' X ',' O ',' X ',' O ',' O ',' O ',' O ',' X ',' X ',"   ","   "]

    def isGameOver(self):
        # Extra safeguarding if e.g. several rows of fives
        # are found on the same move.
        def foundFive():
            # not all path return value, so status type could end being None and the next call results TypeError
            # < not supported between instances of Nonetype and int
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
        # Helper function for removing available moves from the bot.
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
            # move looks atleast slightly reasonable.
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