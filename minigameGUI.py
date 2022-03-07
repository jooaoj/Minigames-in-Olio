import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import math

from minigames.memorygame import Memorygame

class GUI(tk.Tk):   #inheritance, hierarchy
    def __init__(self):
        super().__init__()
        self.title("-¤- The Most Malicious Memorygame -¤-")
        self.geometry("300x400")
        self.game = Memorygame() #aggregation
        self.title(self.game.title)
        self.label = ttk.Label(self, text=self.board(), anchor=tk.CENTER)
        self.__createLayout() #no need to outsiders to make, so hidden
        
    def __createLayout(self):
        ttk.Label(self, text='-¤- The Most Malicious Memorygame -¤-').grid(row=0, column=0, sticky=tk.E, padx=10, pady=10)
        entry = ttk.Entry(self, width=10)
        entry.grid(row=0, column=1, sticky=tk.E)
        #register to listen to an event and binding the event to function call
        entry.bind('<Return>', (lambda event: self.show(entry)))
        self.label.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW)

    def show(self, entry):
        select = entry.get()
        self.game.move(int(select))
        self.label.config(text=self.board())
        #if game is over
        if self.game.isGameOver():
            reset = tk.messagebox.askyesno("game over", "Do you want to start a new game?")
            if reset:  # If reset == True...
                self.game.reset()
            else:
                quit()  # Escape program, as it should.
            
    def board(self):
        row = int(math.sqrt(len(self.game.board)))
        s1 = ""
        x = 0
        var1 = 0
        var2 = row
        s1 += '\t '
        while x < row:
            s1 += ''+chr(65+1*x)+'\t'
            x += 1
        x = 0
        s1 += '\n'
        while x < row:
            s1 += str(x+1)+'\t'
            s1 += "\t".join(self.game.board[var1:var2]) #appearance is not ready yet
            s1 += "\n"
            x = x + 1
            var1 = var1 +row
            var2 = var2 +row
        return s1

    
if __name__ =='__main__':
    g = GUI()
    g.mainloop()
