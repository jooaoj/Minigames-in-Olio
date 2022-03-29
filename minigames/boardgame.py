# -*- coding: utf-8 -*-
"""
Title:          minigames_ver2.py
Author(s):      Paavo Makela, Jooa Jaakkola, Mio Saari, Nea Virtanen & Roope Kakko
Description:    Graphical user-interface, and contains the protoype for all games.
"""
# Python built-ins:
from abc import ABC
import json


class Boardgame:

    # Class variable => declared outside init + usable as is all over class.
    filename = ""
    bgSymbol = "_"
    # Collection of small alphabets:
    symbols = tuple([" " + chr(asciiCharacter) + \
                     " " for asciiCharacter in range(97, 123)])

    def __init__(self):
        self.title = title
        self.size = size
        self.board = {}

    # ~~ #

    @classmethod
    def serialize(cls, obj):
        """
        Save game-state into external file (JSON)
        """
        with open(cls.filename, "w") as file:  # Open a file in write-mode and close it after use.
            json.dump(obj.__dict__, file)

    @classmethod
    def deserialize(cls):
        try:
            with open(cls.filename, "r") as file:  # Open a file in read-mode and close it after use.
                loaded = json.load(file)
                game = cls()
                # Copy loaded JSON to new cls-dict:
                for key in loaded.keys():
                    setattr(game, key, loaded[key])

        except FileNotFoundError:
            game = cls()

        return game  # a.k.a return "altered" game-argument back into main.py

    # ~~ #

    @abstractmethod
    def move(self) -> bool:
        """
        
        :param :
        :return True if valid move:
        """
        pass

    def isGameOver(self) -> int:
        """
        
		:param :
		:return 0, 1, 2 or 3:
        """
        pass

    def reset(self):
        pass