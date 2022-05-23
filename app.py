from doctest import master
import customtkinter
from tkinter.ttk import Style
from custom_notebook import CustomNotebook


class App(customtkinter.CTk):

    def __init__(self, *args, fg_color="#ffffff", **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        
        # Root window config
        self.set_appearance_mode("Light")
        self.geometry("500x400")
        self.resizable(False, False)
        
        # Expand the grid cells
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Create frames
        self.header_frame = customtkinter.CTkFrame(master=self, fg_color="#ffffff")
        self.content_frame = customtkinter.CTkFrame(master=self)

        self.header_frame.grid(row=0, column=0, sticky="we", padx=10)
        self.content_frame.grid(row=1, column=0, sticky="nesw")

        # Create buttons
        self.btn_general = customtkinter.CTkButton(master=self.header_frame,
                                                   text="General",
                                                   width=30,
                                                   height=26,
                                                   text_color="#ffffff")

        self.btn_cpu = customtkinter.CTkButton(master=self.header_frame,
                                               text="CPU",
                                               width=30,
                                               height=26,
                                               text_color="#ffffff")

        self.btn_memory = customtkinter.CTkButton(master=self.header_frame,
                                                  text="Memory",
                                                  width=30,
                                                  height=26,
                                                  text_color="#ffffff")

        self.btn_disk_usage = customtkinter.CTkButton(master=self.header_frame,
                                                  text="Disk usage",
                                                  width=30,
                                                  height=26,
                                                  text_color="#ffffff")

        self.btn_network = customtkinter.CTkButton(master=self.header_frame,
                                                  text="Network",
                                                  width=30,
                                                  height=26,
                                                  text_color="#ffffff")

        self.btn_general.grid(row=0, column=0)
        self.btn_cpu.grid(row=0, column=1)
        self.btn_memory.grid(row=0, column=2)
        self.btn_disk_usage.grid(row=0, column=3)
        self.btn_network.grid(row=0, column=4)
