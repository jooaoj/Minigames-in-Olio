# -*- coding: utf-8 -*-
"""
Title:          minigamesGUI_ver0.py
Author(s):      Paavo Makela, Jooa Jaakkola, Mio Saari, Nea Virtanen & Roope Kakko
Description:    Graphical user-interface.
"""
# Python built-ins:
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import math

# From PATH:
from minigames.memorygame import Memorygame
from minigames.fiverow import FiveRow


# from minigames.minimine import Minimine


class GUI(tk.Tk):  # Inheritance, hierarchy
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.game = Memorygame()  # Aggregation - combination (diamond-shape in diagram)
        self.title(self.game.title)
        self.label = ttk.Label(self, text=self.board(), anchor=tk.CENTER)
        self.__createLayout()

    def __createLayout(self):
        """
        No need for outsiders to make, so hidden.
        """
        ttk.Label(self, text='Type a number that matches a place on board (0 - max)') \
            .grid(row=0, column=0, sticky=tk.E, padx=10, pady=10)

        entry = ttk.Entry(self, width=10)
        entry.grid(row=0, column=1, sticky=tk.E)

        # Register to listen to an event and binding the event to function call.
        entry.bind('<Return>', (lambda event: self.show(entry)))
        self.label.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW)

    def show(self, entry):
        """
        Game-functionality translated to GUI.
        :param entry:
        """
        select = entry.get()
        self.game.move(int(select))
        self.label.config(text=self.board())

        if self.game.isGameOver():  # "if True {...}"
            reset = tk.messagebox.askyesno("game over", "Do you want to start a new game?")
            if reset:  # "if True {...}"
                self.game.reset()
                self.__createLayout()
            else:
                self.destroy()  # Escape program, as it should.

    def board(self):
        """
        Draws the game-board into tkinter-window.
        :return: s1
        """
        row = int(math.sqrt(len(self.game.board)))
        s1 = ""
        x = 0
        var1 = 0
        var2 = row
        s1 += '\t '
        while x < row:
            s1 += '' + chr(65 + 1 * x) + '\t'
            x += 1
        x = 0
        s1 += '\n'
        while x < row:
            s1 += str(x + 1) + '\t'
            s1 += "\t".join(self.game.board[var1:var2])  # Appearance is not ready yet
            s1 += "\n"
            x = x + 1
            var1 = var1 + row
            var2 = var2 + row
        return s1


if __name__ == '__main__':
    g = GUI()

    window = tk.Tk()
    frame = GUI()  # pass : parent=window ?
    frame.grid()  # pass : row=0, column=0 ?
    window.mainloop()

    g.mainloop()
