from tkinter import Tk
from custom_notebook import CustomNotebook

class App(Tk):

    def __init__(self):
        super().__init__()

        # root window config
        self.geometry("500x400")
        self.resizable(False, False)

        self.notebook = CustomNotebook(self)
        self.notebook.pack(expand=True, fill="both")
    