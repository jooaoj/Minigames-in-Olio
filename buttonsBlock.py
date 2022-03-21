"""
Title:          [file.py]
Author:         Jooa Jaakkola (@benevolentimp)
Description:    ["Free-form simplification"]
"""
import tkinter as tk
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
        self.tvar = [''] * len(parent.game.board)
        self.__createLayout()

    def __createLayout(self):
        """
        No need for outsiders to make stuff, so hidden.
        """

        rows = int(math.sqrt(len(self.parent.game.board)))
        self.buttons = []  # remove previous
        for i in range(0, len(self.parent.game.board)):
            t = tk.StringVar()
            self.tvar[i] = t
            self.tvar[i].set(self.parent.game.board[i])
            button = ttk.Button(self, textvariable=self.tvar[i], \
                                command=lambda i=i: self.parent.move(i))
            button.grid(row=i // rows, column=i % rows, sticky=tk.NSEW)
            self.rowconfigure(i // rows, weight=1)
            self.columnconfigure(i % rows, weight=1)
            self.buttons.append(button)
            # x, y, j = 0, 0, 0
        # for item in self.parent.game.board:
        #     button = ttk.Button(self, text=ttk.Label(), command=lambda j=j: self.parent.move(j))
        #     button.grid(row=x, column=y)
        #     y += 1
        #     j += 1
        #     # If n.of columns == sqrt(len(game.board)) => column iteration "to next line"
        #     if y == int(math.sqrt(len(self.parent.game.board))):
        #         y = 0
        #         x += 1

    def disable(self, nro):  # Overwrites abstract-method as it should.
        self.buttons[nro].config(state="disabled")

# testing
# btn = ButtonsBlock()
