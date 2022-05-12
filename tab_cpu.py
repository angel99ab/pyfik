from tkinter import ttk
from cpuinfo import get_cpu_info
import psutil


class TabCPU(ttk.Frame):

    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.cpu_freq = psutil.cpu_freq()
        
        label_frame_brand = ttk.LabelFrame(self, text="Specification")
        brand = ttk.Label(label_frame_brand, text=get_cpu_info()["brand_raw"], foreground="blue")

        label_frame_cores = ttk.LabelFrame(self, text="Cores")
        cores = ttk.Label(label_frame_cores, text=psutil.cpu_count(logical=False), foreground="blue")

        label_frame_threads = ttk.LabelFrame(self, text="Threads")
        threads = ttk.Label(label_frame_threads, text=psutil.cpu_count(), foreground="blue")

        brand.pack(expand=1)
        cores.pack(expand=1)
        threads.pack(expand=1)

        label_frame_brand.place(width=280, height=60, x=10, y=10)
        label_frame_cores.place(width=85, height=60, x=300, y=10)
        label_frame_threads.place(width=85, height=60, x=395, y=10)
