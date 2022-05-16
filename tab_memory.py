from tkinter import ttk
import psutil


class TabMemory(ttk.Frame):

    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.vitual_memory = psutil.virtual_memory()
        self.swap_memory = psutil.swap_memory()

        # RAM memory
        label_frame_ram = ttk.LabelFrame(self, text="RAM")

        label_ram_total = ttk.Label(label_frame_ram, text="Total:")
        ram_total = ttk.Label(label_frame_ram, text=self.get_size(self.vitual_memory.total), foreground="blue")
        label_ram_used = ttk.Label(label_frame_ram, text="Used:")
        ram_used = ttk.Label(label_frame_ram, text=self.get_size(self.vitual_memory.used), foreground="blue")
       
        label_ram_total.place(x=70, y=20)
        ram_total.place(x=110, y=20)
        label_ram_used.place(x=290, y=20)
        ram_used.place(x=330, y=20)

        label_ram_available = ttk.Label(label_frame_ram, text="Available:")
        ram_available = ttk.Label(label_frame_ram, text=self.get_size(self.vitual_memory.available), foreground="blue")
        label_ram_percentage = ttk.Label(label_frame_ram, text="Percentage:")
        ram_percentage = ttk.Label(label_frame_ram, text=str(self.vitual_memory.percent) + " %", foreground="blue")
        
        label_ram_available.place(x=70, y=80)
        ram_available.place(x=130, y=80)
        label_ram_percentage.place(x=290, y=80)
        ram_percentage.place(x=360, y=80)

        label_frame_ram.place(width=470, height=170, x=10, y=10)

        # Swap memory
        label_frame_swap = ttk.LabelFrame(self, text="Swap")

        label_swap_total = ttk.Label(label_frame_swap, text="Total:")
        swap_total = ttk.Label(label_frame_swap, text=self.get_size(self.swap_memory.total), foreground="blue")
        label_swap_free = ttk.Label(label_frame_swap, text="Free:")
        swap_free = ttk.Label(label_frame_swap, text=self.get_size(self.swap_memory.free), foreground="blue")
    
        label_swap_total.place(x=70, y=20)
        swap_total.place(x=110, y=20)
        label_swap_free.place(x=290, y=20)
        swap_free.place(x=320, y=20)

        label_swap_used = ttk.Label(label_frame_swap, text="Used:")
        swap_used = ttk.Label(label_frame_swap, text=self.get_size(self.swap_memory.total), foreground="blue")
        label_swap_percentage = ttk.Label(label_frame_swap, text="Percentage:")
        swap_percentage = ttk.Label(label_frame_swap, text=str(self.swap_memory.percent) + " %", foreground="blue")
    
        label_swap_used.place(x=70, y=80)
        swap_used.place(x=110, y=80)
        label_swap_percentage.place(x=290, y=80)
        swap_percentage.place(x=360, y=80)

        label_frame_swap.place(width=470, height=170, x=10, y=190)


    def get_size(self, bytes, suffix="B"):
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f} {unit}{suffix}"
            bytes /= factor
            