from tkinter import ttk
import psutil
import customtkinter


class TabDiskUsage(customtkinter.CTkFrame):
    
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.disks_info = []
        self.container_childs = []
        self.current_frame = 0

        self.gather_disks_info()

        # Setup layout of the parent
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, minsize=70)

        for i in range(len(self.disks_info)):
            # Create and configure frame top
            frame_top = customtkinter.CTkFrame(master=self, fg_color="#ffffff")
            frame_top.rowconfigure(0, minsize=40)
            frame_top.columnconfigure(0, weight=1)
            frame_top.rowconfigure(1, weight=1)
            frame_top.columnconfigure(1, weight=1)
            frame_top.grid(row=0, column=0, sticky="nesw")

            # Create and configure the frame top inside the frame top
            frame_top_top = customtkinter.CTkFrame(master=frame_top, fg_color="#ffffff")
            frame_top_top.rowconfigure(0, weight=1)
            frame_top_top.columnconfigure(0, weight=1)
            frame_top_top.grid(row=0, columnspan=2, sticky="nesw")

            label_number_disk = customtkinter.CTkLabel(master=frame_top_top,
                                                       text=self.disks_info[i]["n_disk"],
                                                       text_color="#509fe9",
                                                       text_font=('Sans-serif','13','bold'))
            label_number_disk.grid(row=0, column=0)

            # Create and configure frame left inside frame top
            frame_top_left = customtkinter.CTkFrame(master=frame_top, fg_color="#ffffff")
            frame_top_left.rowconfigure(0, weight=1)
            frame_top_left.columnconfigure(0, weight=1)
            frame_top_left.rowconfigure(1, weight=1)
            frame_top_left.columnconfigure(1, weight=1)
            frame_top_left.rowconfigure(2, weight=1)
            frame_top_left.rowconfigure(3, weight=1)
            frame_top_left.rowconfigure(4, weight=1)
            frame_top_left.rowconfigure(5, weight=1)
            frame_top_left.grid(row=1, column=0, sticky="nesw")

            label_mountpoint = customtkinter.CTkLabel(master=frame_top_left,
                                                      text="Mountpoint",
                                                      text_color="#509fe9",
                                                      width=10,
                                                      text_font=('Sans-serif','11','bold'))
                                                
            mountpoint = customtkinter.CTkLabel(master=frame_top_left,
                                                text=self.disks_info[i]["mountpoint"],
                                                width=10)

            label_file_system_type = customtkinter.CTkLabel(master=frame_top_left,
                                                      text="File system type",
                                                      text_color="#509fe9",
                                                      width=10,
                                                      text_font=('Sans-serif','11','bold'))
                                                
            system_type = customtkinter.CTkLabel(master=frame_top_left,
                                                text=self.disks_info[i]["fstype"],
                                                width=10)

            label_total_size = customtkinter.CTkLabel(master=frame_top_left,
                                                      text="Total Size",
                                                      text_color="#509fe9",
                                                      width=10,
                                                      text_font=('Sans-serif','11','bold'))
                                                
            total_size = customtkinter.CTkLabel(master=frame_top_left,
                                                text=self.get_size(self.disks_info[i]["total"]),
                                                width=10)

            label_used = customtkinter.CTkLabel(master=frame_top_left,
                                                text="Used",
                                                text_color="#509fe9",
                                                width=10,
                                                text_font=('Sans-serif','11','bold'))
                                                
            used = customtkinter.CTkLabel(master=frame_top_left,
                                          text=self.get_size(self.disks_info[i]["used"]),
                                          width=10)

            label_free = customtkinter.CTkLabel(master=frame_top_left,
                                                text="Free",
                                                text_color="#509fe9",
                                                width=10,
                                                text_font=('Sans-serif','11','bold'))
                                                
            free = customtkinter.CTkLabel(master=frame_top_left,
                                          text=self.get_size(self.disks_info[i]["free"]),
                                          width=10)

            label_percentage = customtkinter.CTkLabel(master=frame_top_left,
                                      text="Percentage",
                                      text_color="#509fe9",
                                      width=10,
                                      text_font=('Sans-serif','11','bold'))
                                                
            percentage = customtkinter.CTkLabel(master=frame_top_left,
                                      text=str(self.disks_info[i]["percent"]) + " %",
                                      width=10)

            label_mountpoint.grid(row=0, column=0, sticky="e")
            mountpoint.grid(row=0, column=1, sticky="w")
            label_file_system_type.grid(row=1, column=0, sticky="e")
            system_type.grid(row=1, column=1, sticky="w")
            label_total_size.grid(row=2, column=0, sticky="e")
            total_size.grid(row=2, column=1, sticky="w")
            label_used.grid(row=3, column=0, sticky="e")
            used.grid(row=3, column=1, sticky="w")
            label_free.grid(row=4, column=0, sticky="e")
            free.grid(row=4, column=1, sticky="w")
            label_percentage.grid(row=5, column=0, sticky="e")
            percentage.grid(row=5, column=1, sticky="w")

            # Create and configure frame right inside frame top
            frame_top_right = customtkinter.CTkFrame(master=frame_top, fg_color="#ffffff")
            frame_top_right.rowconfigure(0, weight=1)
            frame_top_right.columnconfigure(0, weight=1)
            frame_top_right.rowconfigure(1, weight=1)
            frame_top_right.columnconfigure(1, weight=1)
            frame_top_right.rowconfigure(2, weight=1)
            frame_top_right.rowconfigure(3, weight=1)
            frame_top_right.rowconfigure(4, weight=1)
            frame_top_right.rowconfigure(5, weight=1)
            frame_top_right.grid(row=1, column=1, sticky="nesw")

            label_read_count = customtkinter.CTkLabel(master=frame_top_right,
                                                      text="Read count",
                                                      text_color="#509fe9",
                                                      width=10,
                                                      text_font=('Sans-serif','11','bold'))
                                                
            read_count = customtkinter.CTkLabel(master=frame_top_right,
                                                text=self.get_size(self.disks_info[i]["read_count"]),
                                                width=10)

            label_write_count = customtkinter.CTkLabel(master=frame_top_right,
                                                       text="Write count",
                                                       text_color="#509fe9",
                                                       width=10,
                                                       text_font=('Sans-serif','11','bold'))
                                                
            write_count = customtkinter.CTkLabel(master=frame_top_right,
                                                 text=self.get_size(self.disks_info[i]["write_count"]),
                                                 width=10)

            label_read_bytes = customtkinter.CTkLabel(master=frame_top_right,
                                                      text="Read bytes",
                                                      text_color="#509fe9",
                                                      width=10,
                                                      text_font=('Sans-serif','11','bold'))
                                                
            read_bytes = customtkinter.CTkLabel(master=frame_top_right,
                                                text=self.get_size(self.disks_info[i]["read_bytes"]),
                                                width=10)

            label_write_bytes = customtkinter.CTkLabel(master=frame_top_right,
                                                       text="Write bytes",
                                                       text_color="#509fe9",
                                                       width=10,
                                                       text_font=('Sans-serif','11','bold'))
                                                
            write_bytes = customtkinter.CTkLabel(master=frame_top_right,
                                                 text=self.get_size(self.disks_info[i]["write_bytes"]),
                                                 width=10)

            label_read_time = customtkinter.CTkLabel(master=frame_top_right,
                                                     text="Read time",
                                                     text_color="#509fe9",
                                                     width=10,
                                                     text_font=('Sans-serif','11','bold'))
                                                
            read_time = customtkinter.CTkLabel(master=frame_top_right,
                                               text=self.get_size(self.disks_info[i]["read_time"]),
                                               width=10)

            label_write_time = customtkinter.CTkLabel(master=frame_top_right,
                                                      text="Write time",
                                                      text_color="#509fe9",
                                                      width=10,
                                                      text_font=('Sans-serif','11','bold'))
                                                
            write_time = customtkinter.CTkLabel(master=frame_top_right,
                                                text=self.get_size(self.disks_info[i]["write_time"]),
                                                width=10)

            label_read_count.grid(row=0, column=0, sticky="e")
            read_count.grid(row=0, column=1, sticky="w")
            label_write_count.grid(row=1, column=0, sticky="e")
            write_count.grid(row=1, column=1, sticky="w")
            label_read_bytes.grid(row=2, column=0, sticky="e")
            read_bytes.grid(row=2, column=1, sticky="w")
            label_write_bytes.grid(row=3, column=0, sticky="e")
            write_bytes.grid(row=3, column=1, sticky="w")
            label_read_time.grid(row=4, column=0, sticky="e")
            read_time.grid(row=4, column=1, sticky="w")
            label_write_time.grid(row=5, column=0, sticky="e")
            write_time.grid(row=5, column=1, sticky="w")

            self.container_childs.append(frame_top)

        # Remove all the frame in the grid
        for frame in self.container_childs:
            frame.grid_forget()

        # Display the first disk
        self.container_childs[self.current_frame].grid(row=0, column=0, sticky="nesw")

        # Create and configure bottom frame
        self.frame_bottom = customtkinter.CTkFrame(master=self, fg_color="#ffffff")
        self.frame_bottom.rowconfigure(0, weight=1)
        self.frame_bottom.columnconfigure(0, weight=1)
        self.frame_bottom.columnconfigure(1, weight=1)
        self.frame_bottom.grid(row=1, column=0, sticky="nesw")

        self.button_previous = customtkinter.CTkButton(self.frame_bottom,
                                                       text="<",
                                                       width=100,
                                                       text_color="#ffffff",
                                                       text_font=('Sans-serif','18','bold'),
                                                       command=self.display_previous_frame)

        self.button_next = customtkinter.CTkButton(self.frame_bottom,
                                                   text=">",
                                                   width=100,
                                                   text_color="#ffffff",
                                                   text_font=('Sans-serif','18','bold'),
                                                   command=self.display_next_frame)

        self.button_previous.grid(row=0, column=0)
        self.button_next.grid(row=0, column=1)


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
            self.container_childs[self.current_frame].grid_forget()
            self.current_frame -= 1
            self.container_childs[self.current_frame].grid(row=0, column=0, sticky="nesw")


    def display_next_frame(self):
        if self.current_frame < len(self.disks_info) - 1:
            self.container_childs[self.current_frame].grid_forget()
            self.current_frame += 1
            self.container_childs[self.current_frame].grid(row=0, column=0, sticky="nesw")


    def get_size(self, bytes, suffix="B"):
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f} {unit}{suffix}"
            bytes /= factor
