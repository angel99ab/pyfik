import customtkinter
import platform
import psutil
from datetime import datetime


class TabGeneral(customtkinter.CTkFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Expand grid columns of parent frame
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # Create labels
        self.label_system = customtkinter.CTkLabel(master=self,
                                                   text="System",
                                                   text_color="#509fe9",
                                                   width=10,
                                                   text_font=('Sans-serif','11','bold'))
                                            
        self.system = customtkinter.CTkLabel(master=self,
                                             text=platform.system(),
                                             width=10)

        self.label_release = customtkinter.CTkLabel(master=self,
                                                    text="Release",
                                                    text_color="#509fe9",
                                                    width=10,
                                                    text_font=('Sans-serif','11','bold'))

        self.release = customtkinter.CTkLabel(master=self,
                                              text=platform.release(),
                                              width=10)

        self.label_hostname = customtkinter.CTkLabel(master=self,
                                                     text="Hostname",
                                                     text_color="#509fe9",
                                                     width=10,
                                                     text_font=('Sans-serif','11','bold'))

        self.hostname = customtkinter.CTkLabel(master=self,
                                               text=platform.node(),
                                               width=10)

        self.label_version = customtkinter.CTkLabel(master=self,
                                                    text="Version",
                                                    text_color="#509fe9",
                                                    width=10,
                                                    text_font=('Sans-serif','11','bold'))

        self.version = customtkinter.CTkLabel(master=self,
                                              text=platform.version(),
                                              width=10)

        self.label_machine = customtkinter.CTkLabel(master=self,
                                                    text="Machine",
                                                    text_color="#509fe9",
                                                    width=10,
                                                    text_font=('Sans-serif','11','bold'))

        self.machine = customtkinter.CTkLabel(master=self,
                                              text=platform.machine(),
                                              width=10)

        self.label_boot_time = customtkinter.CTkLabel(master=self,
                                                      text="Boot time",
                                                      text_color="#509fe9",
                                                      width=10,
                                                      text_font=('Sans-serif','11','bold'))

        self.boot_time = customtkinter.CTkLabel(master=self,
                                                text=self.get_boot_time(),
                                                width=10)

        # Display the labels
        self.label_system.grid(row=0, column=0, sticky="e")
        self.system.grid(row=0, column=1, sticky="w")
        self.label_release.grid(row=1, column=0, sticky="e")
        self.release.grid(row=1, column=1, sticky="w")
        self.label_hostname.grid(row=2, column=0, sticky="e")
        self.hostname.grid(row=2, column=1, sticky="w")
        self.label_version.grid(row=3, column=0, sticky="e")
        self.version.grid(row=3, column=1, sticky="w")
        self.label_machine.grid(row=4, column=0, sticky="e")
        self.machine.grid(row=4, column=1, sticky="w")
        self.label_boot_time.grid(row=5, column=0, sticky="e")
        self.boot_time.grid(row=5, column=1, sticky="w")


    def get_boot_time(self):
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        date = f"{bt.day}/{bt.month}/{bt.year}"
        time = f"{bt.hour}:{bt.minute}:{bt.second}"
        return f"{date} {time}"
