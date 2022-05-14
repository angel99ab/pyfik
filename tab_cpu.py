from tkinter import ttk
from cpuinfo import get_cpu_info
import psutil


class TabCPU(ttk.Frame):

    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.cpu_freq = psutil.cpu_freq()
        self.cpu_info = get_cpu_info()
        
        label_frame_brand = ttk.LabelFrame(self, text="Specification")
        brand = ttk.Label(label_frame_brand, text=self.cpu_info["brand_raw"], foreground="blue")

        label_frame_cores = ttk.LabelFrame(self, text="Cores")
        cores = ttk.Label(label_frame_cores, text=psutil.cpu_count(logical=False), foreground="blue")

        label_frame_threads = ttk.LabelFrame(self, text="Threads")
        threads = ttk.Label(label_frame_threads, text=psutil.cpu_count(), foreground="blue")

        label_frame_min_freq = ttk.LabelFrame(self, text="Min frequency")
        min_freq = ttk.Label(label_frame_min_freq, text=str(self.cpu_freq.min) + " Mhz", foreground="blue")

        label_frame_current_freq = ttk.LabelFrame(self, text="Current frequency")
        current_freq = ttk.Label(label_frame_current_freq, text=str(self.cpu_freq.current) + " Mhz", foreground="blue")
        
        label_frame_max_freq = ttk.LabelFrame(self, text="Max frequency")
        max_freq = ttk.Label(label_frame_max_freq, text=str(self.cpu_freq.max) + " Mhz", foreground="blue")

        label_frame_bits = ttk.LabelFrame(self, text="Bits")
        bits = ttk.Label(label_frame_bits, text=self.cpu_info["bits"], foreground="blue")

        label_frame_family = ttk.LabelFrame(self, text="Family")
        family = ttk.Label(label_frame_family, text=self.cpu_info["family"], foreground="blue")

        label_frame_model = ttk.LabelFrame(self, text="Model")
        model = ttk.Label(label_frame_model, text=self.cpu_info["model"], foreground="blue")

        label_frame_stepping = ttk.LabelFrame(self, text="Stepping")
        stepping = ttk.Label(label_frame_stepping, text=self.cpu_info["stepping"], foreground="blue")

        label_frame_flags = ttk.LabelFrame(self, text="Flags")
        flags = ttk.Label(label_frame_flags, text=self.cpu_info["flags"], foreground="blue")

        brand.pack(expand=1)
        cores.pack(expand=1)
        threads.pack(expand=1)
        min_freq.pack(expand=1)
        current_freq.pack(expand=1)
        max_freq.pack(expand=1)
        bits.pack(expand=1)
        family.pack(expand=1)
        model.pack(expand=1)
        stepping.pack(expand=1)
        flags.pack(expand=1)

        label_frame_brand.place(width=280, height=60, x=10, y=10)
        label_frame_cores.place(width=85, height=60, x=300, y=10)
        label_frame_threads.place(width=85, height=60, x=395, y=10)

        label_frame_min_freq.place(width=150, height=60, x=10, y=80)
        label_frame_current_freq.place(width=150, height=60, x=170, y=80)
        label_frame_max_freq.place(width=150, height=60, x=330, y=80)

        label_frame_bits.place(width=110, height=60, x=10, y=150)
        label_frame_family.place(width=110, height=60, x=130, y=150)
        label_frame_model.place(width=110, height=60, x=250, y=150)
        label_frame_stepping.place(width=110, height=60, x=370, y=150)

        label_frame_flags.place(width=470, height=100, x=10, y=220)
