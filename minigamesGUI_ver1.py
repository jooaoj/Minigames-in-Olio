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
from minigames.minimine import Minimine
# -¤- #
from block import Block
from buttonsBlock import ButtonsBlock


class GUI(tk.Frame):  # Inheritance, hierarchy

    def __init__(self, parent):
        super().__init__()  # Calls the parent-class initializer.
        self.game = Memorygame()

        self.parent = parent
        self.parent.geometry("930x325")
        self.parent.title("This should get overwritten!")

        self.parent.title(self.game.title)  # Assign title according to parent.

        self.buttons = ButtonsBlock(parent=self)  # ButtonsBlock's parent == this self
        self.__createLayout()

    def __createLayout(self):
        self.buttons.grid(row=0, column=0, sticky=tk.NSEW)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.buttons._ButtonsBlock__createLayout()
        # x, y = 0, 0
        # self.buttons.grid(row=x, column=y, sticky=tk.S, padx=10, pady=10)

    def move(self, place):
        """
        Check if game is over.
        :return:
        """
        self.buttons.disable(place)

        # a.k.a. if this 'isInstance' sentence == True
        if isinstance(self.game, Memorygame):  # Game : Memorygame
            place1 = place2 = -1
            if len(self.game.pair) == 2 and \
                    self.game.pair[0] != self.game.pair[1] and \
                    self.game.pair[0] in self.game.marks and \
                    self.game.pair[1] in self.game.marks:
                place1 = self.game.board.index(self.game.pair[0])
                place2 = self.game.board.index(self.game.pair[1])
                self.buttons.buttons[place1].config(state="normal")
                self.buttons.buttons[place2].config(state="normal")
            self.game.move(place)
            if place1 != -1 and place2 != -1:  #
                self.buttons.tvar[place1].set(self.game.board[place1])
                self.buttons.tvar[place2].set(self.game.board[place2])

        elif isinstance(self.game, FiveRow):  # Game : FiveRow
            machine = " O "
            self.game.move(place)
            for i, item in enumerate(self.game.board):
                if item == machine:
                    self.buttons.tvar[i].set(self.game.board[i])
                    self.buttons.disable(i)

        else:  # Game : Minimine
            self.game.move(place)

        self.buttons.tvar[place].set(self.game.board[place])  # update buttons
        # is game over
        situation = self.game.isGameOver()
        if situation != 0:
            self.buttons.disableAll()  # game over
            if tk.messagebox.askyesno('New game?', self.game.title):
                self.game.reset()
                self.buttons.enableAll()
                self.__createLayout()
            else:
                self.parent.destroy()  # destroy window
        # if self.game.isGameOver() != 0:
        #     self.buttons.disableAll()
        #
        #     # After disabling buttons, query user:
        #     if tk.messagebox.askyesnocancel("NEW GAME", "GAME OVER " + self.game.title):
        #         self.game.reset()
        #
        #         self.buttons.enableAll()
        #     else:
        #         self.parent.destroy()  # Calls destroy() from parent, which here is self.


# A safeguard and also a sign for coder that this is something to run.
if __name__ == '__main__':
    window = tk.Tk()
    frame = GUI(parent=window)
    frame.grid(row=0, column=0, sticky=tk.NSEW)
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)
    window.mainloop()
