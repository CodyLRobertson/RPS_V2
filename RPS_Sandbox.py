#RPS Sandbox: A place to try out code before implementing into main program (RPS_V2.N)


import random
import string
from random import randint
from random import choice, sample
import datetime
from datetime import datetime
import tkinter as tk

def helloWorld():
    x = range(10)
    for i in x:
        print("Hello World")
        time.sleep(1)
    

#helloWorld()

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