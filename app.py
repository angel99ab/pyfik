import customtkinter
from tab_general import TabGeneral
from tab_cpu import TabCPU


class App(customtkinter.CTk):

    def __init__(self, *args, fg_color="#ffffff", **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)

        # Root window config
        self.set_appearance_mode("Light")
        self.geometry("500x400")
        self.resizable(False, False)
        
        # Expand the grid cells
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # Create frames
        self.header_frame = customtkinter.CTkFrame(master=self, fg_color="#ffffff")
        self.content_frame = customtkinter.CTkFrame(master=self, fg_color="#ffffff")

        self.header_frame.rowconfigure(0, weight=1, minsize=40)

        self.header_frame.grid(row=0, column=0, sticky="we", padx=2)
        self.content_frame.grid(row=1, column=0, sticky="nesw")

        # Create buttons
        self.btn_general = customtkinter.CTkButton(master=self.header_frame,
                                                   text="General",
                                                   width=28,
                                                   height=24,
                                                   text_color="#ffffff",
                                                   command=self.display_general_info)

        self.btn_cpu = customtkinter.CTkButton(master=self.header_frame,
                                               text="CPU",
                                               width=28,
                                               height=24,
                                               text_color="#ffffff")

        self.btn_memory = customtkinter.CTkButton(master=self.header_frame,
                                                  text="Memory",
                                                  width=28,
                                                  height=24,
                                                  text_color="#ffffff")

        self.btn_disk_usage = customtkinter.CTkButton(master=self.header_frame,
                                                  text="Disk usage",
                                                  width=28,
                                                  height=24,
                                                  text_color="#ffffff")

        self.btn_network = customtkinter.CTkButton(master=self.header_frame,
                                                  text="Network",
                                                  width=28,
                                                  height=24,
                                                  text_color="#ffffff")

        self.btn_general.grid(row=0, column=0, padx=2)
        self.btn_cpu.grid(row=0, column=1, padx=2)
        self.btn_memory.grid(row=0, column=2, padx=2)
        self.btn_disk_usage.grid(row=0, column=3, padx=2)
        self.btn_network.grid(row=0, column=4, padx=2)
 
        # Save all frames to show in a list
        self.container_frames = [
            TabGeneral(master=self.content_frame, fg_color="#ffffff"),
        ]
        self.current_frame = 0 

        # Show 'General' frame when opening the app for first time
        self.container_frames[self.current_frame].pack(fill="both", expand=1)


    def display_general_info(self):
        self.container_frames[self.current_frame].pack_forget()
        self.current_frame = 0
        self.container_frames[self.current_frame].pack(fill="both", expand=1)
