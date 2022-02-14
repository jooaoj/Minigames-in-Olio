'''
Title:          memorygame.py
Author(s):      Jooa Jaakkola
Description:    Memorygame()-class for minigames
'''

class Memorygame:

    def __init__(self, board, title, pair, pairs, marks):
        self.board = board
        self.title = title
        self.pair = pair
        self.pairs = pairs
        self.marks = marks

    def move(self, place):
        return place

    def isGameOver(self):
        return 0 # or 1 for "yes/no"

    def reset(self):
        return 0
