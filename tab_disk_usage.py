from tkinter import ttk
import psutil
import customtkinter


class TabDiskUsage(ttk.Frame):

    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.partitions = psutil.disk_partitions()
        # self.disks_io = psutil.disk_io_counters(perdisk=True)

        # next_label_frame = 0


        self.container_childs = []

        i = 0
        self.current_frame = 0

        for partition in self.partitions: 
            label_frame = ttk.Labelframe(self, text=partition.device)
            self.container_childs.append(label_frame)
            self.container_childs[self.current_frame].place(width=470, height=320, x=10, y=10)
            i += 1

        ttk.Button(self, text="<", command=self.display_previous_frame).place(width=20, x=100, y=340)
        ttk.Button(self, text=">", command=self.display_next_frame).place(width=20, x=150, y=340)

        # for partition in self.partitions:
        #     label_frame = ttk.Labelframe(self, text=partition)

        #     # l = ttk.Label(label_frame, text="Test text 1\nTest text 2\nTest text 3\nTest text 4\nTest text 5\nTest text 6\nTest text 7\nTest text 8\nTest text 9", font="-size 20")
        #     # l.pack()

        #     # label_mountpoint = ttk.Label(label_frame, text="Mountpoint")
        #     # mountpoint = ttk.Label(label_frame, text=partition.mountpoint)

        #     # label_file_system_type = ttk.Label(label_frame, text="File system type")
        #     # file_system_type = ttk.Label(label_frame, text=partition.fstype)

        #     # try:
        #     #     partition_usage = psutil.disk_usage(partition.mountpoint)
        #     #     print(f"  Total Size: {self.get_size(partition_usage.total)}")
        #     #     print(f"  Used: {self.get_size(partition_usage.used)}")
        #     #     print(f"  Free: {self.get_size(partition_usage.free)}")
        #     #     print(f"  Percentage: {partition_usage.percent}%")
        #     # except PermissionError:
        #     #     continue
        #     label_frame.place(width=450, height=170, x=10, y=10+next_label_frame)
        #     next_label_frame += 180
            
        # get IO statistics since boot
        # for current_disk in self.disks_io:
        #     print(self.disks_io[current_disk].read_count)
        # print(f"Total write: {self.get_size(disk_io.write_bytes)}")

    def display_previous_frame(self):
        if self.current_frame > 0:
            self.container_childs[self.current_frame].place_forget()
            self.current_frame -= 1
            self.container_childs[self.current_frame].place(width=470, height=320, x=10, y=10)


    def display_next_frame(self):
        if self.current_frame < len(self.partitions) - 1:
            self.container_childs[self.current_frame].place_forget()
            self.current_frame += 1
            self.container_childs[self.current_frame].place(width=470, height=320, x=10, y=10)


    def get_size(self, bytes, suffix="B"):
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f} {unit}{suffix}"
            bytes /= factor
