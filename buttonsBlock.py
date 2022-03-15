"""
Title:          [file.py]
Author:         Jooa Jaakkola (@benevolentimp)
Description:    ["Free-form simplification"]
"""
from tkinter import ttk
import math

from block import Block


class ButtonsBlock(Block):
    def __init__(self, parent):
        """
        As per convention, you should always put the init-super.
        """
        super().__init__(parent)  # Pass information to Block.
        self.parent = parent
        self.buttons = []  # To collect the buttons from Frame.
        self.__createLayout()

    def __createLayout(self):
        """
        No need for outsiders to make stuff, so hidden.
        """
        x, y, j = 0, 0, 0
        for item in self.parent.game.board:
            button = ttk.Button(self, text=item, command=lambda j=j: self.parent.move(j))
            button.grid(row=x, column=y)
            y += 1
            j += 1
            # If n.of columns == sqrt(len(game.board)) => column iteration "to next line"
            if y == int(math.sqrt(len(self.parent.game.board))):
                y = 0
                x += 1

    def disable(self, nro):  # Overwrites abstract-method as it should.
        pass


# testing
# btn = ButtonsBlock()
