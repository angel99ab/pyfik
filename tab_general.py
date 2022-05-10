from tkinter import ttk
import platform
from cpuinfo import get_cpu_info


class TabGeneral(ttk.Frame):

    def __init__(self, master, **kw):
        super().__init__(master, **kw)

        # Styles
        self['padding'] = 15

        lbl_frame_system_info = ttk.LabelFrame(self, text="System Information")

        lbl_system = ttk.Label(lbl_frame_system_info, text="System")
        system = ttk.Label(lbl_frame_system_info, text=platform.system(), foreground="blue")
        lbl_release = ttk.Label(lbl_frame_system_info, text="Release")
        release = ttk.Label(lbl_frame_system_info, text=platform.release(), foreground="blue")
        lbl_hostname = ttk.Label(lbl_frame_system_info, text="Hostname")
        hostname = ttk.Label(lbl_frame_system_info, text=platform.node(), foreground="blue")
        lbl_version = ttk.Label(lbl_frame_system_info, text="Version")
        version = ttk.Label(lbl_frame_system_info, text=platform.version(), foreground="blue")
        lbl_architecture = ttk.Label(lbl_frame_system_info, text="Architecture")
        architecture = ttk.Label(lbl_frame_system_info, text=get_cpu_info()["arch"], foreground="blue")

        lbl_system.grid(row=0, column=0)
        system.grid(row=0, column=1)
        lbl_release.grid(row=1, column=0)
        release.grid(row=1, column=1)
        lbl_hostname.grid(row=2, column=0)
        hostname.grid(row=2, column=1)
        lbl_version.grid(row=3, column=0)
        version.grid(row=3, column=1)
        lbl_architecture.grid(row=4, column=0)
        architecture.grid(row=4, column=1)

        lbl_frame_system_info.pack(fill="both", expand="yes")
