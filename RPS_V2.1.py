import time
import random
import string
from random import randint
from random import choice, sample
import datetime
from datetime import datetime
import tkinter as tk

#1.0) Create Main Menu Widget
    #1.1) Create Brief About Window showing Time and Date, Name of game, and Developer
    #1.2) Create Buttons
        #1.2) Create New Game
        #1.3) About
            #1.3.1) Shows Time,Date,Name of Game, Developer, and Option for TODO list
        #1.4) Exit (Clean)


#1.0      
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()