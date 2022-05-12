from tkinter import ttk
from cpuinfo import get_cpu_info
import psutil


class TabCPU(ttk.Frame):

    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        
        label_frame_brand = ttk.LabelFrame(self, text="Specification")
        brand = ttk.Label(label_frame_brand, text=get_cpu_info()["brand_raw"], foreground="blue")


        brand.pack(expand=1)


        label_frame_brand.place(width=280, height=50, x=10, y=10)
