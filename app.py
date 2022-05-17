from tkinter import Tk
from tkinter.ttk import Style
from custom_notebook import CustomNotebook


class App(Tk):

    def __init__(self):
        super().__init__()

        style = Style()
        style.theme_use("default")
        style.configure("TNotebook.Tab", focuscolor="#d6d6d6");
        style.configure("TButton", focuscolor="#d6d6d6");

        # root window config
        self.geometry("500x400")
        self.resizable(False, False)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # widget inside root window
        self.notebook = CustomNotebook(self)
        self.notebook.grid(column=0, row=0, sticky="nesw")
    