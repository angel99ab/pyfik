from tkinter import Tk
from custom_notebook import CustomNotebook

class App(Tk):

    def __init__(self):
        super().__init__()

        # root window config
        self.geometry('700x500')
        self.resizable(False, False)

        self.notebook = CustomNotebook(self)
        self.notebook.pack(expand=True, fill="both")
    