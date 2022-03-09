"""
Title:          [file.py]
Author:         Jooa Jaakkola (@benevolentimp)
Description:    ["Free-form simplification"]
"""
from tkinter import ttk

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
        j = 0
        for item in self.parent.game.board:
            button = ttk.Button(self, text=item, \
                                command=lambda j=j: self.parent.move(j))
            button.grid(row=0, column=j)
            j += 1

    def disable(self, nro):  # Overwrites abstract-method as it should.
        pass


# testing
# btn = ButtonsBlock()
