# -*- coding: utf-8 -*-
"""
Console-UI for minigames_ver1 (procedural programming):
Each minigame is one class whose :

attributes ->
    board
    title
and methods ->
    move()
    isGameOver()
    reset()

Importing minigames do not create any side effects.
All interaction with the user and game classes go through this script.

ver1 :
serialization and deserialization of each game object is implemented calling
each game's class methods serialize and deserialize, serialized file is
a class-variable filename is each class
"""
# Python built-ins:
import math
import os

# Importing from PATH:
from minigames.memorygame import Memorygame
from minigames.minimine import Minimine
from minigames.fiverow import FiveRow


# Main-program:
def draw(game, rows, columns):
    clear()
    print('\t', game.title, '\n\n')
    print('\t       ', ' '.join(columns))
    for i in range(1, rows + 1):
        print('\t    ', f'{i:2}', ''.join(game.board[(i - 1) * rows:(i - 1) * rows + rows]))


def play(game):
    rows = int(math.sqrt(len(game.board)))
    columns = [str(' ' + chr(i + 64)) for i in range(1, rows + 1)]

    while True:
        draw(game, rows, columns)
        try:
            select = input('\n\n\tColumn and row e.g. A1 (X quit): ').upper()
            if len(select) == 1 and select == 'X':
                game.serialize(game)  # use through object who knows its class
                break  # return False closes the complete program
            if len(select) >= 2:
                column = ' ' + select[0].upper()
                row = int(select[1:])
                if column in columns and 1 <= row <= rows:  # Showed in more mathematical format.
                    place = columns.index(column) + (row - 1) * len(columns)
                    if not game.move(place):
                        raise ValueError()  # invalid move                   
                    situation = game.isGameOver()
                    draw(game, rows, columns)
                    if situation == 0:
                        continue
                    if not restart(game):
                        break
        except Exception as e:
            print('Check your selection', e)
    return True


def restart(game):
    game.reset()
    game.serialize(game)
    if input('\n\n\tDo you want to play again [Y|N]? ').upper() == 'Y':
        return True
    else:
        return False


def menu():
    game = None

    while True:
        clear()
        print('''
        Minigame collection:
              
        1. Minimine
        2. Memorygame - find the pairs
        3. Five-in-a-row
        4. Quit
        ''')
        select = ''
        while select not in ('1', '2', '3'):
            select = input('\tSelect: ')
            break
        match select:  # 3.10 or newer
            case '1':
                game = Minimine.deserialize()
            case '2':
                game = Memorygame.deserialize()
            case '3':
                game = FiveRow.deserialize()
            case _:
                break

        if not play(game):
            break


def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


# Run this main-program:
if __name__ == '__main__':
    menu()
