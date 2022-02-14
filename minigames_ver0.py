# -*- coding: utf-8 -*-
'''
Console user interface for minigames ver 0 (procedural programming)
Each minigame is one class whose 
attributes
    board
    title    
and methods
    move
    isGameOver
    reset
are used in the user interface.
Importing minigames do not create any side effects.
All interaction with the user and game classes go through this script.
'''

import math
import os #to get the name of the operating system for clearing the console screen
import minigames
from minigames.memorygame import Memorygame
#from minigames.minimine import Minimine
#from minigames.fiverow import FiveRow

def draw(game, rows, columns): 
    clear()
    print('\t', game.title, '\n\n')
    print('\t       ', ' '.join(columns))
    for i in range(1, rows+1):
        print('\t    ', f'{i:2}', ''.join(game.board[(i-1)*rows:(i-1)*rows+rows]))
            
def play(game):
    rows = int(math.sqrt(len(game.board)))
    columns = [str(' ' + chr(i + 64)) for i in range(1, rows+1)]
    
    while True:   
        draw(game, rows, columns)
        try:
            select = input('\n\n\tColumn and row e.g. A1 (X quit): ').upper()                           
            if len(select) == 1 and select == 'X':
                break # return False closes the complete program
            if len(select) >= 2:                            
                column = ' '+ select[0].upper()
                row = int(select[1:])
                if column in columns and row >= 1 and row <= rows:
                    place = columns.index(column) + (row-1)*len(columns)
                    if not game.move(place):                             
                        raise ValueError()  # invalid move                   
                    situation = game.isGameOver()
                    draw(game, rows, columns)
                    if situation == 0:
                        continue
                    elif situation == 1: # win
                        print("\n\n\tWell done!")
                    elif situation == 2: # lose
                        print('\n\n\tOOPS - better luck next time!')
                    elif situation == 3: # tie
                        print("\n\n\tIt's tie - no more moves")
                    if not restart(game):
                        break
        except:
            print('check your selection')
    return True # Lab 2 - adding serialization
 
def restart(game)                                                      :    
    if input('\n\n\tDo you want to play again [Y|N]? ').upper() == 'Y':
        game.reset()        
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
        match select:
            #case '1':
             #    game = Minimine()
            case '2':
                 game = Memorygame()                
            #case '3':
             #    game = FiveRow()
            case _:
                break
        if not play(game):
            break


def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
        
if __name__ == '__main__':
    menu()
