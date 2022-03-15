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

# From PATH:
from minigames.memorygame import Memorygame
from minigames.fiverow import FiveRow
# -¤- #
from block import Block
from buttonsBlock import ButtonsBlock


# Not usable yet:
# from minigames.minimine import Minimine


class GUI(tk.Frame):  # Inheritance, hierarchy
    def __init__(self, parent):
        super().__init__()  # Calls the parent-class initializer.
        self.parent = parent
        self.parent.geometry("400x400")
        self.parent.title("This should get overwritten!")

        self.game = FiveRow()
        self.parent.title(self.game.title)  # Assign title according to parent.

        self.buttons = ButtonsBlock(parent=self)  # ButtonsBlock's parent == this self
        self.__createLayout()

    def __createLayout(self):
        x, y = 0, 0
        self.buttons.grid(row=x, column=y, sticky=tk.S, padx=10, pady=10)

    def move(self, place):
        """
        Check if game is over.
        :return:
        """
        self.game.move(place)
        if self.game.isGameOver() != 0:
            self.buttons.disableAll()

            # After disabling buttons, query user:
            if tk.messagebox.askyesnocancel("NEW GAME", "GAME OVER " + self.game.title):
                self.game.reset()

                self.buttons.enableAll()
            else:
                self.parent.destroy()  # Calls destroy() from parent, which here is self.


# A safeguard and also a sign for coder that this is something to run.
if __name__ == '__main__':
    window = tk.Tk()
    frame = GUI(parent=window)
    frame.grid(row=0, column=0)
    window.mainloop()
