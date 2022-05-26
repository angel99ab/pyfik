import customtkinter
from tkinter import ttk
import psutil


class TabMemory(customtkinter.CTkFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vitual_memory = psutil.virtual_memory()
        self.swap_memory = psutil.swap_memory()

        # Setup layout of parent frame
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # Create and configure top frame
        self.frame_top = customtkinter.CTkFrame(master=self, fg_color="#fff")
        self.frame_top.columnconfigure(0, weight=1)
        self.frame_top.columnconfigure(1, weight=1)
        self.frame_top.columnconfigure(2, weight=1)
        self.frame_top.columnconfigure(3, weight=1)
        self.frame_top.columnconfigure(4, weight=1)
        self.frame_top.columnconfigure(5, weight=1)
        self.frame_top.grid(row=0, column=0, sticky="nesw")

        self.label_ram = customtkinter.CTkLabel(master=self.frame_top,
                                                text="RAM",
                                                text_color="#509fe9",
                                                width=10,
                                                text_font=('Sans-serif','11','bold'))

        self.label_ram_total = customtkinter.CTkLabel(master=self.frame_top,
                                                      text="Total",
                                                      text_color="#509fe9",
                                                      width=10,
                                                      text_font=('Sans-serif','11','bold'))

        self.ram_total = customtkinter.CTkLabel(master=self.frame_top,
                                                text=self.get_size(self.vitual_memory.total),
                                                width=10)

        self.label_ram_used = customtkinter.CTkLabel(master=self.frame_top,
                                                     text="Used",
                                                     text_color="#509fe9",
                                                     width=10,
                                                     text_font=('Sans-serif','11','bold'))

        self.ram_used = customtkinter.CTkLabel(master=self.frame_top,
                                               text=self.get_size(self.vitual_memory.used),
                                               width=10)

        self.label_ram_available = customtkinter.CTkLabel(master=self.frame_top,
                                                          text="Available",
                                                          text_color="#509fe9",
                                                          width=10,
                                                          text_font=('Sans-serif','11','bold'))

        self.ram_available = customtkinter.CTkLabel(master=self.frame_top,
                                                    text=self.get_size(self.vitual_memory.available),
                                                    width=10)
    
        self.label_ram.grid(row=0, column=0, columnspan=6, pady=20)

        self.label_ram_total.grid(row=1, column=0, sticky="e", pady=20)
        self.ram_total.grid(row=1, column=1, sticky="w", pady=20)

        self.label_ram_used.grid(row=1, column=2, sticky="e", pady=20)
        self.ram_used.grid(row=1, column=3, sticky="w", pady=20)
        
        self.label_ram_available.grid(row=1, column=4, sticky="e", pady=20)
        self.ram_available.grid(row=1, column=5, sticky="w", pady=20)

        # Create and configure bottom frame
        self.frame_bottom = customtkinter.CTkFrame(master=self, fg_color="#ffffff")
        self.frame_bottom.columnconfigure(0, weight=1)
        self.frame_bottom.columnconfigure(1, weight=1)
        self.frame_bottom.columnconfigure(2, weight=1)
        self.frame_bottom.columnconfigure(3, weight=1)
        self.frame_bottom.columnconfigure(4, weight=1)
        self.frame_bottom.columnconfigure(5, weight=1)
        self.frame_bottom.grid(row=1, column=0, sticky="nesw")

        self.label_swap = customtkinter.CTkLabel(master=self.frame_bottom,
                                                 text="SWAP",
                                                 text_color="#509fe9",
                                                 width=10,
                                                 text_font=('Sans-serif','11','bold'))

        self.label_swap_total = customtkinter.CTkLabel(master=self.frame_bottom,
                                                       text="Total",
                                                       text_color="#509fe9",
                                                       width=10,
                                                       text_font=('Sans-serif','11','bold'))

        self.swap_total = customtkinter.CTkLabel(master=self.frame_bottom,
                                                 text=self.get_size(self.swap_memory.total),
                                                 width=10)

        self.label_swap_free = customtkinter.CTkLabel(master=self.frame_bottom,
                                                      text="Free",
                                                      text_color="#509fe9",
                                                      width=10,
                                                      text_font=('Sans-serif','11','bold'))

        self.swap_free = customtkinter.CTkLabel(master=self.frame_bottom,
                                                text=self.get_size(self.swap_memory.free),
                                                width=10)

        self.label_swap_used = customtkinter.CTkLabel(master=self.frame_bottom,
                                                      text="Used",
                                                      text_color="#509fe9",
                                                      width=10,
                                                      text_font=('Sans-serif','11','bold'))

        self.swap_used = customtkinter.CTkLabel(master=self.frame_bottom,
                                                text=self.get_size(self.swap_memory.used),
                                                width=10)
    
        self.label_swap.grid(row=0, column=0, columnspan=6, pady=20)

        self.label_swap_total.grid(row=1, column=0, sticky="e", pady=20)
        self.swap_total.grid(row=1, column=1, sticky="w", pady=20)

        self.label_swap_free.grid(row=1, column=2, sticky="e", pady=20)
        self.swap_free.grid(row=1, column=3, sticky="w", pady=20)
        
        self.label_swap_used.grid(row=1, column=4, sticky="e", pady=20)
        self.swap_used.grid(row=1, column=5, sticky="w", pady=20)
        

    def get_size(self, bytes, suffix="B"):
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f} {unit}{suffix}"
            bytes /= factor
            