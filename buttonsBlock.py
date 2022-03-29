"""
Title:          [file.py]
Author:         Jooa Jaakkola (@benevolentimp)
Description:    ["Free-form simplification"]
"""
import tkinter as tk
from tkinter import ttk
import math

from block import Block


def calculateRowAndColumn(place: int, boardLength: int):
    columns = math.isqrt(boardLength)
    row = place // columns

    if row == 0:
        column = place
    else:
        column = place % (row * columns)

    return row, column


class ButtonsBlock(Block):
    def __init__(self, parent=None, game=None):
        super().__init__(parent)
        self.parent = parent
        self.game = game
        self.buttons = []
        self.board = [tk.StringVar() for _ in range(len(self.game.board['visible']))]

        for index in range(len(self.game.board['visible'])):
            # Copy from board
            self.board[index].set(self.game.board['visible'][index])
            # Calculate row and col for grid placement.
            row, column = calculateRowAndColumn(index, len(self.game.board['visible']))
            # Set clicked as callback
            button = tk.Button(self, textvariable=self.board[index], command=lambda place=index: self.clicked(place), width=3)
            padding = 5
            button.grid(row=row, column=column, pady=padding, padx=padding, ipady=padding, ipadx=padding)
            self.buttons.append(button)

        # Update once so the button states are correct from start
        self.update()

    def clicked(self, place):
        # Make a move
        self.game.move(place)

        # And update board
        self.update()

        # Check game-state and act accordingly
        status = self.game.isGameOver()
        if status:
            self.disableAll()
            match status:
                case 1: msg = "You won!\nPlay again?"
                case 2: msg = "You lost!\nPlay again?"
                case 3: msg = "It's a tie!\nPlay again?"

            restart = tk.messagebox.askyesno('Game Over', msg)
            if restart:
                self.game.reset()
                self.update()
                self.enableAll()
            else:
                self.game.reset()
                self.parent.quit()

    def disable(self, nro):
        self.buttons[nro].config(state="disabled")

    def update(self):
        self.enableAll()
        for index, slot in enumerate(self.board):
            # Checking for empty is not optimal, but it accounts
            # for the initial state of the game.
            if self.game.board['visible'][index] != self.game.bgSymbol:
                self.disable(index)
            slot.set(self.game.board['visible'][index])