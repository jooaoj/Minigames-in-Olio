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

        self.buttons = ButtonsBlock(parent=self)  # Buttonblock's parent == this self
        self.__createLayout()

    def __createLayout(self):
        self.buttons.grid(row=0, column=0, \
                          sticky=tk.S, padx=10, pady=10)

    def move(self, place):
        """
        Check if game is over.
        :return:
        """
        self.game.move(place)
        if self.game.isGameOver() != 0:
            self.buttons.disableAll()

            # After disabling buttons, query user:
            if tk.messagebox.askyesnocancel("NEW GAME", "GAME OVER "+self.game.title):
                self.game.reset()
                self.buttons.enableAll()
            else:
                self.parent.destroy()  # Calls destroy() from parent, which here is self.


    #     self.tvar = tk.StringVar()      # Holding button's text with StringVar \
    #     self.tvar.set(str(self.count))  # Ideally make multiple in a for-loop.
    #     self.tvar = self.parent.board
    #     self.count = 0
    #
    #     i = 0
    #     button = ttk.Button(self, textvariable=self.tvar, \
    #                         command=lambda i=0: self.move(i))
    #     button.grid(row=0, column=0, \
    #                 sticky=tk.E + tk.W + tk.N + tk.S, \
    #                 ipadx=10, ipady=10)
    #     self.button = ttk.Button(self, text="Press me", command=self.hello). \
    #         grid(row=1, column=2)
    #
    #     # self.label = ttk.Label(self, text=self.board(), anchor=tk.CENTER)
    #     # self.__createLayout()

    # def show(self, entry):
    #     """
    #     Game-functionality translated to GUI.
    #     :param entry:
    #     """
    #     select = entry.get()
    #     self.game.move(int(select))
    #     self.label.config(text=self.board())
    #
    #     if self.game.isGameOver():  # "if True {...}"
    #         reset = tk.messagebox.askyesno("game over", "Do you want to start a new game?")
    #         if reset:  # "if True {...}"
    #             self.game.reset()
    #             self.__createLayout()
    #         else:
    #             self.destroy()  # Escape program, as it should.


# A safeguard and also a sign for coder that this is something to run.
if __name__ == '__main__':
    window = tk.Tk()
    frame = GUI(parent=window)
    frame.grid(row=0, column=0)
    window.mainloop()
