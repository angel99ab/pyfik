from tkinter import ttk
import platform
import psutil
from datetime import datetime


class TabGeneral(ttk.Frame):

    def __init__(self, master, **kw):
        super().__init__(master, **kw)

        label_frame_system = ttk.LabelFrame(self, text="System")
        system = ttk.Label(label_frame_system, text=platform.system(), foreground="blue")

        label_frame_release = ttk.LabelFrame(self, text="Release")
        release = ttk.Label(label_frame_release, text=platform.release(), foreground="blue")

        label_frame_hostname = ttk.LabelFrame(self, text="Hostname")
        hostname = ttk.Label(label_frame_hostname, text=platform.node(), foreground="blue")

        label_frame_version = ttk.LabelFrame(self, text="Version")
        version = ttk.Label(label_frame_version, text=platform.version(), foreground="blue")

        label_frame_machine = ttk.LabelFrame(self, text="Machine")
        machine = ttk.Label(label_frame_machine, text=platform.machine(), foreground="blue")

        label_frame_boot_time = ttk.LabelFrame(self, text="Boot time")
        boot_time = ttk.Label(label_frame_boot_time, text=self.get_boot_time(), foreground="blue")

        system.pack(expand=1)
        release.pack(expand=1)
        hostname.pack(expand=1)
        version.pack(expand=1)
        machine.pack(expand=1)
        boot_time.pack(expand=1)

        label_frame_system.place(width=280, height=70, x=10, y=10)
        label_frame_release.place(width=180, height=70, x=300, y=10)
        label_frame_hostname.place(width=280, height=70, x=10, y=90)
        label_frame_version.place(width=180, height=70, x=300, y=90)
        label_frame_machine.place(width=180, height=70, x=300, y=170)
        label_frame_boot_time.place(width=280, height=70, x=10, y=170)


    def get_boot_time(self):
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        return f"{bt.day}/{bt.month}/{bt.year} {bt.hour}:{bt.minute}:{bt.second}"

