"""
Title:          memorygame.py
Author(s):      Jooa Jaakkola
Description:    Memorygame()-class for mini-games
"""


class Memorygame:
    def __init__(self):
        self.board = [" # "]*16
        self.title = "The Most Malicious Memory-game"
        self.pair = ""
        self.pairs = ""
        self.marks = ('%', '@', '¤')

    def move(self, place):
        if place == self.board:
            return True
        else:
            return False

    def isGameOver():
        pass

    def reset(self):
        pass
