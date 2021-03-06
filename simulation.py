"""
TODOS:
Make model of a single IEEE 802.22 network
Be able to choose the number of channels and signals, then run simulation

implement saved environments, so simulation doesn't always start from scratch

implement algorithms from studies to simulate complex behavior of IEEE 802.22 networks.
For instance, removing signal from channel and adding to another, methods of finding
which channel is the best fit for a signal, etc.

simply add more data to signals and channels to more closely match network spec
"""

import uuid
from tkinter import *
from tkinter import ttk
from math import sqrt


# make a signal class
class Signal:
    # Currently contains location, bandwith usage, and whether signal is incumbent
    def __init__(self, location: tuple, bandwith_usage: float, is_incumbent: bool):
        self.location = location
        self.bandwith_usage = bandwith_usage
        self.is_incumbent = is_incumbent
        self.id = uuid.uuid4()
    
    def print_data(self):
        return f'id is {self.id} \nlocation is {self.location} \nbandwith_usage is {self.bandwith_usage} \nis_incumbent is {self.is_incumbent}'



class Channel:
    def __init__(self, location: tuple, bandwith: float):
        self.location = location
        self.bandwith = bandwith
        self.signals = []

    def get_available_bandwith(self):
        if not self.signals:
            return self.bandwith
        else:
            sum = 0
            for signal in self.signals:
                sum += signal.bandwith_usage
            return self.bandwith - sum

    def print_signals_data(self):
        if self.signals:
            signal_data = ""
            for signal in self.signals:
                signal_data += "\nSignal in channel:\n" + signal.print_data() + '\n'
            return signal_data
        else:
            return "No signals present"
    
    def get_data(self):
        location = f'Channel location is {self.location}\n'
        available_bandwith = f'Available bandwith is {self.get_available_bandwith()}\n'
        return location + available_bandwith + self.print_signals_data()

    def add_signal(self, new_signal: Signal):
        if new_signal.bandwith_usage <= self.get_available_bandwith():
            self.signals.append(new_signal)
        else:
            print("Not enough bandwith available to add signal!")

    def remove_signal(self, index):
        self.signals.pop(index)



channel_1 = Channel(location=(0, 0), bandwith=50)
channel_2 = Channel(location=(20, 20), bandwith=100)

channels = [channel_1, channel_2]

# TODO: channel selection algorithm
# Create hierarchy of available channels, sort them, and add to first channel
def add_signal_to_best_channel(signal: Signal):
    available_channels = []
    for channel in channels:
        if channel.get_available_bandwith() >= signal.bandwith_usage:
            x1 = signal.location[0]
            y1 = signal.location[1]
            x2 = channel.location[0]
            y2 = channel.location[1]

            # Calculate distance between signal and channel using formula
            available_channels.append((channel, sqrt((x2 - x1)**2 + (y2 - y1)**2)))
        
    # Sort list of tuples in available channels by second value (distance), then add signal to first channel in list
    if available_channels:
        available_channels.sort(key = lambda x: x[1]) 
        available_channels[0][0].add_signal(signal)



# Tkinter gui code below
def update_textareas():
        T.delete("1.0", END)
        T.insert(END, channel_1.get_data())
        T_2.delete("1.0", END)
        T_2.insert(END, channel_2.get_data())

def add_signal_gui(*args):
    incumbent = False
    if is_incumbent_gui.get() == "y": incumbent = True
    else: pass

    gui_signal = Signal(location=(x_coord.get(), y_coord.get()), bandwith_usage=bandwith_gui.get(), is_incumbent=incumbent)
    try:
        add_signal_to_best_channel(gui_signal)
        update_textareas()
    except ValueError:
        pass

def remove_signal_gui():
    try: 
        channels[channel_selector_gui.get()].remove_signal(signal_selector_gui.get())
        update_textareas()
    except ValueError:
        pass

root = Tk()
root.title("IEEE 802.22 Simulation")

mainframe = ttk.Frame(root, padding = "7 7 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

x_coord = DoubleVar()
x_coord_entry = ttk.Entry(mainframe, width=7, textvariable=x_coord)
x_coord_entry.grid(column=2, row=1, sticky=(W, E))
ttk.Label(mainframe, text="x coordinate").grid(column=1, row=1, sticky=W)

y_coord = DoubleVar()
y_coord_entry = ttk.Entry(mainframe, width=7, textvariable=y_coord)
y_coord_entry.grid(column=2, row=2, sticky=(W, E))
ttk.Label(mainframe, text="y coordinate").grid(column=1, row=2, sticky=W)


bandwith_gui = DoubleVar()
bandwith_entry = ttk.Entry(mainframe, width=7, textvariable=bandwith_gui)
bandwith_entry.grid(column=2, row=3, sticky=(W, E))
ttk.Label(mainframe, text="Bandwith usage").grid(column=1, row=3, sticky=W)

is_incumbent_gui = StringVar()
is_incumbent_entry = ttk.Entry(mainframe, width=7, textvariable=is_incumbent_gui)
is_incumbent_entry.grid(column=2, row=4, sticky=(W, E))
ttk.Label(mainframe, text="Incumbent signal? y/n").grid(column=1, row=4, sticky=W)

ttk.Button(mainframe, text="Add signal", command=add_signal_gui).grid(column=3, row=3, sticky=W)

channel_selector_gui = IntVar()
channel_selector_entry = ttk.Entry(mainframe, width=7, textvariable=channel_selector_gui)
channel_selector_entry.grid(column=5, row=1, sticky=(W, E))
ttk.Label(mainframe, text="Channel to remove from? 0/1").grid(column=4, row=1, sticky=W)

signal_selector_gui = IntVar()
signal_selector_entry = ttk.Entry(mainframe, width=7, textvariable=signal_selector_gui)
signal_selector_entry.grid(column=5, row=2, sticky=(W, E))
ttk.Label(mainframe, text="Index of signal to remove from channel").grid(column=4, row=2, sticky=W)

ttk.Button(mainframe, text="Remove signal", command=remove_signal_gui).grid(column=5, row=3, sticky=W)

T = Text(root, height=40, width=50)
T.grid(column = 0, row = 6, sticky = S)
T.insert(END, channel_1.get_data())

T_2 = Text(root, height=40, width=50)
T_2.grid(column = 3, row = 6, sticky = S)
T_2.insert(END, channel_2.get_data())


for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.bind("<Return>", add_signal_gui)

root.mainloop()