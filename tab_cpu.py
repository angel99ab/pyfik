from doctest import master
import customtkinter
from threading import Thread
from tkinter import ttk, Toplevel
from cpuinfo import get_cpu_info
import psutil


class TabCPU(customtkinter.CTkFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cpu_freq = psutil.cpu_freq()
        self.cpu_info = get_cpu_info()
        
        # Setup layout of parent frame
        self.rowconfigure(0, minsize=50)
        self.columnconfigure(0, minsize=240)
        self.rowconfigure(1, minsize=260)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        # Create and configure top frame
        self.frame_top = customtkinter.CTkFrame(master=self, fg_color="#ffffff")
        self.frame_top.rowconfigure(0, weight=1)
        self.frame_top.columnconfigure(0, weight=1)
        self.frame_top.columnconfigure(1, weight=1)
        self.frame_top.grid(row=0, column=0, sticky="nesw", columnspan=2)

        self.label_brand = customtkinter.CTkLabel(master=self.frame_top,
                                                  text="Specification",
                                                  text_color="#509fe9",
                                                  width=10,
                                                  text_font=('Sans-serif','11','bold'))

        self.brand = customtkinter.CTkLabel(master=self.frame_top,
                                            text=self.cpu_info["brand_raw"],
                                            foreground="blue")

        self.label_brand.grid(row=0, column=0, sticky="e")
        self.brand.grid(row=0, column=1, sticky="w")

        # Create and configure left frame 
        self.frame_left = customtkinter.CTkFrame(master=self, fg_color="#ffffff")
        self.frame_left.columnconfigure(1, weight=1)
        self.frame_left.grid(row=1, column=0, sticky="nesw")

        self.label_cores = customtkinter.CTkLabel(master=self.frame_left,
                                                  text="Cores",
                                                  text_color="#509fe9",
                                                  width=30,
                                                  text_font=('Sans-serif','11','bold'))
                                            
        self.cores = customtkinter.CTkLabel(master=self.frame_left,
                                            text=psutil.cpu_count(logical=False),
                                            width=10)

        self.label_threads = customtkinter.CTkLabel(master=self.frame_left,
                                                    text="Threads",
                                                    text_color="#509fe9",
                                                    width=30,
                                                    text_font=('Sans-serif','11','bold'))
                                            
        self.threads = customtkinter.CTkLabel(master=self.frame_left,
                                              text=psutil.cpu_count(),
                                              width=10)

        self.label_min_freq = customtkinter.CTkLabel(master=self.frame_left,
                                                     text="Min frequency",
                                                     text_color="#509fe9",
                                                     width=30,
                                                     text_font=('Sans-serif','11','bold'))
                                            
        self.min_freq = customtkinter.CTkLabel(master=self.frame_left,
                                               text=str(self.cpu_freq.min) + " Mhz",
                                               width=10)

        self.label_current_freq = customtkinter.CTkLabel(master=self.frame_left,
                                                         text="Current frequency",
                                                         text_color="#509fe9",
                                                         width=30,
                                                         text_font=('Sans-serif','11','bold'))
                                            
        self.current_freq = customtkinter.CTkLabel(master=self.frame_left,
                                                   text=str(self.cpu_freq.current) + " Mhz",
                                                   width=10)

        self.label_max_freq = customtkinter.CTkLabel(master=self.frame_left,
                                                     text="Max frequency",
                                                     text_color="#509fe9",
                                                     width=30,
                                                     text_font=('Sans-serif','11','bold'))
                                            
        self.max_freq = customtkinter.CTkLabel(master=self.frame_left,
                                               text=str(self.cpu_freq.max) + " Mhz",
                                               width=10)

        self.label_bits = customtkinter.CTkLabel(master=self.frame_left,
                                                 text="Bits",
                                                 text_color="#509fe9",
                                                 width=30,
                                                 text_font=('Sans-serif','11','bold'))
                                            
        self.bits = customtkinter.CTkLabel(master=self.frame_left,
                                           text=self.cpu_info["bits"],
                                           width=10)

        self.label_family = customtkinter.CTkLabel(master=self.frame_left,
                                                   text="Family",
                                                   text_color="#509fe9",
                                                   width=30,
                                                   text_font=('Sans-serif','11','bold'))
                                            
        self.family = customtkinter.CTkLabel(master=self.frame_left,
                                             text=self.cpu_info["family"],
                                             width=10)

        self.label_model = customtkinter.CTkLabel(master=self.frame_left,
                                                  text="Model",
                                                  text_color="#509fe9",
                                                  width=30,
                                                  text_font=('Sans-serif','11','bold'))
                                            
        self.model = customtkinter.CTkLabel(master=self.frame_left,
                                            text=self.cpu_info["model"],
                                            width=10)

        self.label_stepping = customtkinter.CTkLabel(master=self.frame_left,
                                                     text="Stepping",
                                                     text_color="#509fe9",
                                                     width=30,
                                                     text_font=('Sans-serif','11','bold'))
                                            
        self.stepping = customtkinter.CTkLabel(master=self.frame_left,
                                               text=self.cpu_info["stepping"],
                                               width=10)

        self.label_cores.grid(row=0, column=0, sticky="e")
        self.cores.grid(row=0, column=1, sticky="w")
        self.label_threads.grid(row=1, column=0, sticky="e")
        self.threads.grid(row=1, column=1, sticky="w")
        self.label_min_freq.grid(row=2, column=0, sticky="e")
        self.min_freq.grid(row=2, column=1, sticky="w")
        self.label_current_freq.grid(row=3, column=0, sticky="e")
        self.current_freq.grid(row=3, column=1, sticky="w")
        self.label_max_freq.grid(row=4, column=0, sticky="e")
        self.max_freq.grid(row=4, column=1, sticky="w")
        self.label_bits.grid(row=5, column=0, sticky="e")
        self.bits.grid(row=5, column=1, sticky="w")
        self.label_family.grid(row=6, column=0, sticky="e")
        self.family.grid(row=6, column=1, sticky="w")
        self.label_family.grid(row=7, column=0, sticky="e")
        self.family.grid(row=7, column=1, sticky="w")
        self.label_family.grid(row=8, column=0, sticky="e")
        self.family.grid(row=8, column=1, sticky="w")

        # Create and configure right frame 
        self.frame_right = customtkinter.CTkFrame(master=self, fg_color="#ffffff")
        self.frame_right.columnconfigure(0, weight=1)
        self.frame_right.columnconfigure(1, weight=1)
        self.frame_right.columnconfigure(2, weight=1)
        self.frame_right.grid(row=1, column=1, sticky="nesw")

        self.label_flags = customtkinter.CTkLabel(master=self.frame_right,
                                                  text="Flags",
                                                  text_color="#509fe9",
                                                  width=30,
                                                  text_font=('Sans-serif','11','bold'))
                                            
        self.label_flags.grid(row=0, column=0, sticky="nesw", columnspan=3)
        
        flags = self.cpu_info["flags"]
        n = 0

        for i in range(1, 9, 1):
            for j in range(3):
                label_flag = customtkinter.CTkLabel(master=self.frame_right,
                                                    text=flags[n],
                                                    width=5)
                label_flag.grid(row=i, column=j)
                n += 1

        # Create and configure bottom frame 
        self.frame_bottom = customtkinter.CTkFrame(master=self, fg_color="#ffffff")
        self.frame_bottom.rowconfigure(0, weight=1)
        self.frame_bottom.columnconfigure(0, weight=1)
        self.frame_bottom.grid(row=2, column=0, sticky="nesw", columnspan=2)

        self.button_show_cores = customtkinter.CTkButton(master=self.frame_bottom,
                                                         text="Show cores",
                                                         width=130,
                                                         text_color="#ffffff",
                                                         command=self.display_cores_window)

        self.button_show_cores.grid(row=0, column=0, sticky="n")


    def display_cores_window(self):
        self.window = customtkinter.CTkToplevel(master=self)
        self.window.title("CPU cores")
        self.window.geometry("320x400")
        self.window.resizable(False, False)
        self.window.grab_set()

        self.labels = []
 

        # for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        #     lbl_core = customtkinter.CTkLabel(self.window, text=f"Core {i} [")
        #     lbl__bar_percentage = customtkinter.CTkLabel(self.window, text=f"||||||||||")
        #     lbl_number_percentage = customtkinter.CTkLabel(self.window, text=f"57.2 %]")
        #     self.labels.append(lbl)
        #     self.window.grid_columnconfigure()
    
        lbl_core = customtkinter.CTkLabel(self.window, text=f"Core 8 [").pack(side="left")
        lbl__bar_percentage = customtkinter.CTkLabel(self.window, text="|||||||||||||||||||").pack(side="left")
        lbl_number_percentage = customtkinter.CTkLabel(self.window, text=f"57.2 %]").pack(side="left")
        # thread = Thread(target=self.update_cpu_percent, daemon=True)
        # thread.start()
        

    def update_cpu_percent(self):
        i = 0
        list_completed = False
        max_cores = len(psutil.cpu_percent(percpu=True))

        while self.window.winfo_exists():
            if not list_completed:
                percentage_cores = psutil.cpu_percent(percpu=True, interval=1)
                list_completed = True

            if self.window.winfo_exists():
                self.labels[i].config(text=f"Core {i}: {percentage_cores[i]} %")

                i += 1

                if i == max_cores:
                    i = 0
                    list_completed = False
