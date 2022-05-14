from tkinter import ttk
from tab_general import TabGeneral
from tab_cpu import TabCPU
from tab_memory import TabMemory


class CustomNotebook(ttk.Notebook):

    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        
        # Styles
        self["padding"] = 2

        self.tab_general = TabGeneral(self)
        self.tab_cpu_info = TabCPU(self)
        self.tab_memory_info = TabMemory(self)

        self.add(self.tab_general, text='General')
        self.add(self.tab_cpu_info, text='CPU')
        self.add(self.tab_memory_info, text='Memory')
