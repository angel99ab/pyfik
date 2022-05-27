from tkinter import ttk
import customtkinter
import socket
import psutil
from psutil._common import bytes2human


class TabNetwork(customtkinter.CTkFrame):
    
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

        # Setup layout of the parent
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, minsize=50)

        for i in range(len(self.network_info)):
            # Create and configure frame top
            frame_top = customtkinter.CTkFrame(master=self, fg_color="#ffffff")
            frame_top.rowconfigure(0, minsize=40)
            frame_top.columnconfigure(0, minsize=250)
            frame_top.rowconfigure(1, minsize=140)
            frame_top.columnconfigure(1, weight=1)
            frame_top.rowconfigure(2, weight=1)
            frame_top.grid(row=0, column=0, sticky="nesw")

            # Create and configure the frame network name inside the frame top
            frame_network_name = customtkinter.CTkFrame(master=frame_top, fg_color="#ffffff")
            frame_network_name.rowconfigure(0, weight=1)
            frame_network_name.columnconfigure(0, weight=1)
            frame_network_name.grid(row=0, columnspan=2, sticky="nesw")

            label_network_name = customtkinter.CTkLabel(master=frame_network_name,
                                                        text=self.network_info[i]["nic"],
                                                        text_color="#509fe9",
                                                        text_font=('Sans-serif','13','bold'))
            label_network_name.grid(row=0, columnspan=2)

            # Create and configure the frame stats inside the frame top
            frame_stats = customtkinter.CTkFrame(master=frame_top, fg_color="#ffffff")
            frame_stats.columnconfigure(0, weight=1)
            frame_stats.columnconfigure(1, weight=1)
            frame_stats.grid(row=1, column=0, sticky="nesw")

            label_stats = customtkinter.CTkLabel(master=frame_stats,
                                                      text="Stats",
                                                      text_color="#509fe9",
                                                      width=10,
                                                      text_font=('Sans-serif','11','bold'))
            
            label_speed = customtkinter.CTkLabel(master=frame_stats,
                                                 text="Speed",
                                                 text_color="#509fe9",
                                                 width=10,
                                                 text_font=('Sans-serif','11','bold'))

            speed = customtkinter.CTkLabel(master=frame_stats,
                                           text=str(self.network_info[i]["stats"]["speed"]) + " MB",
                                           width=10)

            label_duplex = customtkinter.CTkLabel(master=frame_stats,
                                                 text="Duplex",
                                                 text_color="#509fe9",
                                                 width=10,
                                                 text_font=('Sans-serif','11','bold'))

            duplex = customtkinter.CTkLabel(master=frame_stats,
                                           text=self.network_info[i]["stats"]["duplex"],
                                           width=10)

            label_mtu = customtkinter.CTkLabel(master=frame_stats,
                                                 text="Mtu",
                                                 text_color="#509fe9",
                                                 width=10,
                                                 text_font=('Sans-serif','11','bold'))

            mtu = customtkinter.CTkLabel(master=frame_stats,
                                           text=self.network_info[i]["stats"]["mtu"],
                                           width=10)

            label_up = customtkinter.CTkLabel(master=frame_stats,
                                                 text="Up",
                                                 text_color="#509fe9",
                                                 width=10,
                                                 text_font=('Sans-serif','11','bold'))

            up = customtkinter.CTkLabel(master=frame_stats,
                                        text=self.network_info[i]["stats"]["up"],
                                        width=10)

            label_stats.grid(row=0, columnspan=2)
            label_speed.grid(row=1, column=0)
            speed.grid(row=1, column=1)
            label_duplex.grid(row=2, column=0)
            duplex.grid(row=2, column=1)
            label_mtu.grid(row=3, column=0)
            mtu.grid(row=3, column=1)
            label_up.grid(row=4, column=0)
            up.grid(row=4, column=1)

            # Create and configure the frame incoming inside the frame top
            frame_incoming = customtkinter.CTkFrame(master=frame_top, fg_color="#ffffff")
            frame_incoming.columnconfigure(0, weight=1)
            frame_incoming.columnconfigure(1, weight=1)
            frame_incoming.grid(row=1, column=1, sticky="nesw")

            label_incoming = customtkinter.CTkLabel(master=frame_incoming,
                                                    text="Incoming",
                                                    text_color="#509fe9",
                                                    width=10,
                                                    text_font=('Sans-serif','11','bold'))
            
            incoming_label_bytes = customtkinter.CTkLabel(master=frame_incoming,
                                                        text="Bytes",
                                                        text_color="#509fe9",
                                                        width=10,
                                                        text_font=('Sans-serif','11','bold'))

            incoming_bytes = customtkinter.CTkLabel(master=frame_incoming,
                                                    text=self.network_info[i]["incoming"]["bytes"],
                                                    width=10)

            incoming_label_pkts = customtkinter.CTkLabel(master=frame_incoming,
                                                        text="Pkts",
                                                        text_color="#509fe9",
                                                        width=10,
                                                        text_font=('Sans-serif','11','bold'))

            incoming_pkts = customtkinter.CTkLabel(master=frame_incoming,
                                                    text=self.network_info[i]["incoming"]["pkts"],
                                                    width=10)
            
            incoming_label_errs = customtkinter.CTkLabel(master=frame_incoming,
                                                        text="Errs",
                                                        text_color="#509fe9",
                                                        width=10,
                                                        text_font=('Sans-serif','11','bold'))

            incoming_errs = customtkinter.CTkLabel(master=frame_incoming,
                                                    text=self.network_info[i]["incoming"]["errs"],
                                                    width=10)

            incoming_label_drops = customtkinter.CTkLabel(master=frame_incoming,
                                                        text="Drops",
                                                        text_color="#509fe9",
                                                        width=10,
                                                        text_font=('Sans-serif','11','bold'))

            incoming_drops = customtkinter.CTkLabel(master=frame_incoming,
                                                    text=self.network_info[i]["incoming"]["drops"],
                                                    width=10)

            label_incoming.grid(row=0, columnspan=2)
            incoming_label_bytes.grid(row=1, column=0)
            incoming_bytes.grid(row=1, column=1)
            incoming_label_pkts.grid(row=2, column=0)
            incoming_pkts.grid(row=2, column=1)
            incoming_label_errs.grid(row=3, column=0)
            incoming_errs.grid(row=3, column=1)
            incoming_label_drops.grid(row=4, column=0)
            incoming_drops.grid(row=4, column=1)
            
            # Create and configure the frame outgoing inside the frame top
            frame_outgoing = customtkinter.CTkFrame(master=frame_top, fg_color="#ffffff")
            frame_outgoing.columnconfigure(0, weight=1)
            frame_outgoing.columnconfigure(1, weight=1)
            frame_outgoing.grid(row=2, column=0, sticky="nesw")

            label_outgoing = customtkinter.CTkLabel(master=frame_outgoing,
                                                    text="Incoming",
                                                    text_color="#509fe9",
                                                    width=10,
                                                    text_font=('Sans-serif','11','bold'))
            
            outgoing_label_bytes = customtkinter.CTkLabel(master=frame_outgoing,
                                                        text="Bytes",
                                                        text_color="#509fe9",
                                                        width=10,
                                                        text_font=('Sans-serif','11','bold'))

            outgoing_bytes = customtkinter.CTkLabel(master=frame_outgoing,
                                                    text=self.network_info[i]["outgoing"]["bytes"],
                                                    width=10)

            outgoing_label_pkts = customtkinter.CTkLabel(master=frame_outgoing,
                                                        text="Pkts",
                                                        text_color="#509fe9",
                                                        width=10,
                                                        text_font=('Sans-serif','11','bold'))

            outgoing_pkts = customtkinter.CTkLabel(master=frame_outgoing,
                                                    text=self.network_info[i]["outgoing"]["pkts"],
                                                    width=10)

            outgoing_label_errs = customtkinter.CTkLabel(master=frame_outgoing,
                                                        text="Errs",
                                                        text_color="#509fe9",
                                                        width=10,
                                                        text_font=('Sans-serif','11','bold'))

            outgoing_errs = customtkinter.CTkLabel(master=frame_outgoing,
                                                    text=self.network_info[i]["outgoing"]["errs"],
                                                    width=10)

            outgoing_label_drops = customtkinter.CTkLabel(master=frame_outgoing,
                                                        text="Drops",
                                                        text_color="#509fe9",
                                                        width=10,
                                                        text_font=('Sans-serif','11','bold'))

            outgoing_drops = customtkinter.CTkLabel(master=frame_outgoing,
                                                    text=self.network_info[i]["outgoing"]["drops"],
                                                    width=10)

            label_outgoing.grid(row=0, columnspan=2)
            outgoing_label_bytes.grid(row=1, column=0)
            outgoing_bytes.grid(row=1, column=1)
            outgoing_label_pkts.grid(row=2, column=0)
            outgoing_pkts.grid(row=2, column=1)
            outgoing_label_errs.grid(row=3, column=0)
            outgoing_errs.grid(row=3, column=1)
            outgoing_label_drops.grid(row=4, column=0)
            outgoing_drops.grid(row=4, column=1)

            # Create and configure the frame addresses inside the frame top
            frame_addresses = customtkinter.CTkFrame(master=frame_top, fg_color="#ffffff")
            frame_addresses.rowconfigure(0, weight=1)
            frame_addresses.columnconfigure(0, weight=1)
            frame_addresses.rowconfigure(1, weight=1)
            frame_addresses.columnconfigure(1, weight=1)
            frame_addresses.rowconfigure(2, weight=1)
            frame_addresses.grid(row=2, column=1, sticky="nesw")

            addresses_label_mac = customtkinter.CTkLabel(master=frame_addresses,
                                                        text="MAC",
                                                        text_color="#509fe9",
                                                        width=10,
                                                        text_font=('Sans-serif','11','bold'))

            try:
                addresses_mac = customtkinter.CTkLabel(master=frame_addresses,
                                                        text=self.network_info[i]["MAC"],
                                                        width=10)
            except KeyError:
                self.network_info[i]["MAC"] = ""
                addresses_mac = customtkinter.CTkLabel(master=frame_addresses,
                                                       text=self.network_info[i]["MAC"],
                                                       width=10)

            addresses_label_ipv4 = customtkinter.CTkLabel(master=frame_addresses,
                                                        text="IPv4",
                                                        text_color="#509fe9",
                                                        width=10,
                                                        text_font=('Sans-serif','11','bold'))

            addresses_ipv4 = customtkinter.CTkLabel(master=frame_addresses,
                                                    text=self.network_info[i]["IPv4"],
                                                    width=10)

            addresses_label_ipv6 = customtkinter.CTkLabel(master=frame_addresses,
                                                        text="IPv6",
                                                        text_color="#509fe9",
                                                        width=10,
                                                        text_font=('Sans-serif','11','bold'))

            addresses_ipv6 = customtkinter.CTkLabel(master=frame_addresses,
                                                    text=self.network_info[i]["IPv6"],
                                                    width=10)

            addresses_label_mac.grid(row=0, column=0)
            addresses_mac.grid(row=0, column=1)  
            addresses_label_ipv4.grid(row=1, column=0)
            addresses_ipv4.grid(row=1, column=1)
            addresses_label_ipv6.grid(row=2, column=0)
            addresses_ipv6.grid(row=2, column=1)

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
            self.container_childs[self.current_frame].grid_forget()
            self.current_frame -= 1
            self.container_childs[self.current_frame].grid(row=0, column=0, sticky="nesw")


    def display_next_frame(self):
        if self.current_frame < len(self.network_info) - 1:
            self.container_childs[self.current_frame].grid_forget()
            self.current_frame += 1
            self.container_childs[self.current_frame].grid(row=0, column=0, sticky="nesw")
