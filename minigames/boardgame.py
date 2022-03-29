# -*- coding: utf-8 -*-
"""
Title:          boardgame.py
Author(s):      Paavo Makela, Jooa Jaakkola, Mio Saari, Nea Virtanen & Roope Kakko
Description:    Contains the prototype for all games.
"""
# Python built-ins:
from abc import ABC, abstractmethod
import json


class Boardgame(ABC):
    filename: str = 'boardgame.json'
    bgSymbol: str = '   '
    symbols: list = [" " + chr(asciiCharacter) + " " for asciiCharacter in range(97, 123)]

    def __init__(self, size: int = 4, bgSymbol: str = '', symbols: list = []):
        self.size = size

        if bgSymbol:
            Boardgame.bgSymbol = bgSymbol
        if symbols:
            Boardgame.symbols = symbols

        self.board = {
            'visible': [self.bgSymbol for _ in range(self.size * self.size)],
            'hidden': [self.bgSymbol for _ in range(self.size * self.size)],
        }

    @classmethod
    def serialize(cls, obj):
        """
        Writes objects dictionary to savefile. Format is JSON.
        """
        with open(cls.filename, "w") as file:
            json.dump(obj.__dict__, file)

    @classmethod
    def deserialize(cls):
        try:
            # Read json file
            with open(cls.filename, "r") as file:
                loaded = json.load(file)
                # Copy loaded json contents to new classes dict.
                game = cls()
                for key in loaded.keys():
                    setattr(game, key, loaded[key])

        except FileNotFoundError:
            # If there is no json file to be read from, use default.
            game = cls()

        return game

    @abstractmethod
    def move(self, place: int) -> bool:
        pass

    def isGameOver(self):
        pass

    def reset(self):
        self.board['visible'] = [self.bgSymbol for _ in range(len(self.board['visible']))]
