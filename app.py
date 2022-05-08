from tkinter import Tk
from tkinter import ttk


class App(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.window_settings()

    
    def window_settings(self):
        self.geometry('700x500')
        self.resizable(False, False)
    