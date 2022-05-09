from tkinter import ttk


class CustomNotebook(ttk.Notebook):

    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        
        tab1 = ttk.Frame(self)
        tab2 = ttk.Frame(self)

        self.add(tab1, text='General')
        self.add(tab2, text='CPU info')