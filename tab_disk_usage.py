from tkinter import ttk
import psutil
import customtkinter


class TabDiskUsage(ttk.Frame):

    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.disks_info = []
        self.container_childs = []
        self.current_frame = 0

        self.gather_disks_info()

        for i in range(len(self.disks_info)): 
            labelframe = ttk.Labelframe(self, text=self.disks_info[i]["n_disk"])

            ttk.Label(labelframe, text="Mountpoint").place(x=130, y=10)
            ttk.Label(labelframe, text=self.disks_info[i]["mountpoint"], foreground="blue").place(x=250, y=10)

            ttk.Label(labelframe, text="File system type").place(x=130, y=30)
            ttk.Label(labelframe, text=self.disks_info[i]["fstype"], foreground="blue").place(x=250, y=30)

            ttk.Label(labelframe, text="Total Size").place(x=130, y=50)
            ttk.Label(labelframe, text=self.get_size(self.disks_info[i]["total"]), foreground="blue").place(x=250, y=50)

            ttk.Label(labelframe, text="Used").place(x=130, y=70)
            ttk.Label(labelframe, text=self.get_size(self.disks_info[i]["used"]), foreground="blue").place(x=250, y=70)

            ttk.Label(labelframe, text="Free").place(x=130, y=90)
            ttk.Label(labelframe, text=self.get_size(self.disks_info[i]["free"]), foreground="blue").place(x=250, y=90)

            ttk.Label(labelframe, text="Percentage").place(x=130, y=110)
            ttk.Label(labelframe, text=str(self.disks_info[i]["percent"]) + " %", foreground="blue").place(x=250, y=110)

            ttk.Label(labelframe, text="Read count").place(x=130, y=130)
            ttk.Label(labelframe, text=self.get_size(self.disks_info[i]["read_count"]), foreground="blue").place(x=250, y=130)

            ttk.Label(labelframe, text="Write count").place(x=130, y=150)
            ttk.Label(labelframe, text=self.get_size(self.disks_info[i]["write_count"]), foreground="blue").place(x=250, y=150)

            ttk.Label(labelframe, text="Read bytes").place(x=130, y=170)
            ttk.Label(labelframe, text=self.get_size(self.disks_info[i]["read_bytes"]), foreground="blue").place(x=250, y=170)

            ttk.Label(labelframe, text="Write bytes").place(x=130, y=190)
            ttk.Label(labelframe, text=self.get_size(self.disks_info[i]["write_bytes"]), foreground="blue").place(x=250, y=190)

            ttk.Label(labelframe, text="Read time").place(x=130, y=210)
            ttk.Label(labelframe, text=self.get_size(self.disks_info[i]["read_time"]), foreground="blue").place(x=250, y=210)
            
            ttk.Label(labelframe, text="Write time").place(x=130, y=230)
            ttk.Label(labelframe, text=self.get_size(self.disks_info[i]["write_time"]), foreground="blue").place(x=250, y=230)

            self.container_childs.append(labelframe)

        self.container_childs[self.current_frame].place(width=470, height=320, x=10, y=10)

        ttk.Button(self, text="<", command=self.display_previous_frame).place(width=20, x=100, y=340)
        ttk.Button(self, text=">", command=self.display_next_frame).place(width=20, x=150, y=340)


    def gather_disks_info(self):
        partitions = psutil.disk_partitions()
        disks_io = psutil.disk_io_counters(perdisk=True)
        n_disks = 1
        i = 0

        for current_disk in disks_io:
            partition_usage = psutil.disk_usage(partitions[i].mountpoint)
            dictionary = {
                "n_disk": "Disk " + str(n_disks),
                "device": partitions[i].device,
                "mountpoint": partitions[i].mountpoint,
                "fstype": partitions[i].fstype,
                "opts": partitions[i].opts,
                "maxfile": partitions[i].maxfile,
                "maxpath": partitions[i].maxpath,
                "total": partition_usage.total,
                "used": partition_usage.used,
                "free": partition_usage.free,
                "percent": partition_usage.percent,
                "read_count": disks_io[current_disk].read_count,
                "write_count": disks_io[current_disk].write_count,
                "read_bytes": disks_io[current_disk].read_bytes,
                "write_bytes": disks_io[current_disk].write_bytes,
                "read_time": disks_io[current_disk].read_time,
                "write_time": disks_io[current_disk].write_time
            }
            self.disks_info.append(dictionary)
            n_disks += 1
            i += 1


    def display_previous_frame(self):
        if self.current_frame > 0:
            self.container_childs[self.current_frame].place_forget()
            self.current_frame -= 1
            self.container_childs[self.current_frame].place(width=470, height=320, x=10, y=10)


    def display_next_frame(self):
        if self.current_frame < len(self.disks_info) - 1:
            self.container_childs[self.current_frame].place_forget()
            self.current_frame += 1
            self.container_childs[self.current_frame].place(width=470, height=320, x=10, y=10)


    def get_size(self, bytes, suffix="B"):
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f} {unit}{suffix}"
            bytes /= factor
