'''
Title:          memorygame.py
Author(s):      Jooa Jaakkola
Description:    Memorygame()-class for minigames
'''

class Memorygame:

    board = [[["#"],["#"]],[["#"],["#"]]]
    title = "The Most Malicious Memorygame"
    pair = ""
    pairs = len(board)
    marks = ('%', '@', '¤')

    def move(self, place):
        if place == self.board:
            return True
        else:
            return False

    def isGameOver(self):
        if 0:
            return 0

    def reset(self):
        return clear()
