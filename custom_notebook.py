from tkinter import ttk
from tab_general import TabGeneral
from tab_cpu import TabCPU


class CustomNotebook(ttk.Notebook):

    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        
        # Styles
        self["padding"] = 2

        self.tab_general = TabGeneral(self)
        self.tab_cpu_info = TabCPU(self)

        self.add(self.tab_general, text='General')
        self.add(self.tab_cpu_info, text='CPU')
