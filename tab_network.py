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
