"""
Title:          block.py
Author:         Paavo Makela, Jooa Jaakkola, Mio Saari, Nea Virtanen & Roope Kakko
Description:    ButtonsBlock-example
"""
from abc import ABC, abstractmethod
from tkinter import ttk


# Class declars:
class Block(ttk.Frame, ABC):
    def __init__(self):
        """
        Calling frame's init-method.
        """
        ttk.Frame.__init__(self, parent)  # Parent where frame is in.
        self.buttons = None

    @abstractmethod
    def disable(self, nro):
        pass

    def disableAll(self):
        """
        Disable all buttons (assuming inheriting class has button)
        :return: JUST A TEMPLATE
        """
        for button in range(len(self.buttons)):
            self.buttons[button].config(state="disabled")

    def enableAll(self):
        """
        Enable all (assuming it has buttons)
        :return: JUST A TEMPLATE
        """
        for button in range(len(self.buttons)):
            self.buttons[button].config(state="normal")
