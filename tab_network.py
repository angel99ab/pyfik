from __future__ import print_function
from tkinter import ttk
import socket
import psutil
from psutil._common import bytes2human


class TabNetwork(ttk.Frame):
    
    def __init__(self, master, **kw):
        super().__init__(master, **kw)

        self.network_info = []
        self.container_childs = []
        self.current_frame = 0

        self.af_map = {
            socket.AF_INET: 'IPv4',
            socket.AF_INET6: 'IPv6',
            psutil.AF_LINK: 'MAC',
        }

        self.duplex_map = {
            psutil.NIC_DUPLEX_FULL: "full",
            psutil.NIC_DUPLEX_HALF: "half",
            psutil.NIC_DUPLEX_UNKNOWN: "?",
        }

        self.gather_network_info()

        for i in range(len(self.network_info)): 
            labelframe = ttk.Labelframe(self, text=self.network_info[i]["nic"])

            ttk.Label(labelframe, text="Stats").place(x=30, y=10)
            ttk.Label(labelframe, text="Speed").place(x=70, y=30)
            ttk.Label(labelframe, text=str(self.network_info[i]["stats"]["speed"]) + " MB", foreground="blue").place(x=140, y=30)
            ttk.Label(labelframe, text="Duplex").place(x=70, y=50)
            ttk.Label(labelframe, text=self.network_info[i]["stats"]["duplex"], foreground="blue").place(x=140, y=50)
            ttk.Label(labelframe, text="Mtu").place(x=70, y=70)
            ttk.Label(labelframe, text=self.network_info[i]["stats"]["mtu"], foreground="blue").place(x=140, y=70)
            ttk.Label(labelframe, text="Up").place(x=70, y=90)
            ttk.Label(labelframe, text=self.network_info[i]["stats"]["up"], foreground="blue").place(x=140, y=90)

            ttk.Label(labelframe, text="Incoming").place(x=240, y=10)
            ttk.Label(labelframe, text="Bytes").place(x=300, y=30)
            ttk.Label(labelframe, text=self.network_info[i]["incoming"]["bytes"], foreground="blue").place(x=370, y=30)
            ttk.Label(labelframe, text="Pkts").place(x=300, y=50)
            ttk.Label(labelframe, text=self.network_info[i]["incoming"]["pkts"], foreground="blue").place(x=370, y=50)
            ttk.Label(labelframe, text="Errs").place(x=300, y=70)
            ttk.Label(labelframe, text=self.network_info[i]["incoming"]["errs"], foreground="blue").place(x=370, y=70)
            ttk.Label(labelframe, text="Drops").place(x=300, y=90)
            ttk.Label(labelframe, text=self.network_info[i]["incoming"]["drops"], foreground="blue").place(x=370, y=90)

            self.container_childs.append(labelframe)

        self.container_childs[self.current_frame].place(width=470, height=320, x=10, y=10)

        ttk.Button(self, text="<", command=self.display_previous_frame).place(width=20, x=100, y=340)
        ttk.Button(self, text=">", command=self.display_next_frame).place(width=20, x=150, y=340)


    def gather_network_info(self):
        stats = psutil.net_if_stats()
        io_counters = psutil.net_io_counters(pernic=True)

        for nic, addrs in psutil.net_if_addrs().items():
            dictionary = {
                "nic": nic,
            }

            if nic in stats:
                st = stats[nic]
                dictionary["stats"] = {
                    "speed": st.speed,
                    "duplex": self.duplex_map[st.duplex],
                    "mtu": st.mtu,
                    "up": 'yes' if st.isup else 'no'
                }

            if nic in io_counters:
                io = io_counters[nic]
                dictionary["incoming"] = {
                    "bytes": bytes2human(io.bytes_recv),
                    "pkts": io.packets_recv,
                    "errs": io.errin,
                    "drops": io.dropin
                }
                dictionary["outgoing"] = {
                    "bytes": bytes2human(io.bytes_sent),
                    "pkts": io.packets_sent,
                    "errs": io.errout,
                    "drops": io.dropout
                }

            for addr in addrs:
                dictionary[self.af_map.get(addr.family, addr.family)] = addr.address

            self.network_info.append(dictionary)


    def display_previous_frame(self):
        if self.current_frame > 0:
            self.container_childs[self.current_frame].place_forget()
            self.current_frame -= 1
            self.container_childs[self.current_frame].place(width=470, height=320, x=10, y=10)


    def display_next_frame(self):
        if self.current_frame < len(self.network_info) - 1:
            self.container_childs[self.current_frame].place_forget()
            self.current_frame += 1
            self.container_childs[self.current_frame].place(width=470, height=320, x=10, y=10)
