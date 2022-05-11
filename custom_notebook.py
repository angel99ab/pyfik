from tkinter import ttk
from tab_general import TabGeneral


class CustomNotebook(ttk.Notebook):

    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        
        self.tab_general = TabGeneral(self)
        self.tab_cpu_info = ttk.Frame(self)

        self.add(self.tab_general, text='General')
        self.add(self.tab_cpu_info, text='CPU info')
