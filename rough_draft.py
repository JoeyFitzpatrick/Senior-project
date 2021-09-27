"""
TODOS:
Make model of a single IEEE 802.22 network
Make channels within that network
Make signals within that network
Be able to choose the number of channels and signals, then run simulation
This simulation should then show what signals will use what channels
How to implement:
Make network class
"""

import uuid
from tkinter import *
from tkinter import ttk


# make a signal class
class Signal:
    # Currently contains location, bandwith usage, and whether signal is incumbent
    def __init__(self, location: tuple, bandwith_usage: float, is_incumbent: bool):
        self.location = location
        self.bandwith_usage = bandwith_usage
        self.is_incumbent = is_incumbent
        self.id = uuid.uuid4()
    
    def print_data(self):
        return f'id is {self.id}, location is {self.location} \nbandwith_usage is {self.bandwith_usage} \nis_incumbent is {self.is_incumbent}'



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

    def add_signal(self, new_signal: Signal):
        if new_signal.bandwith_usage <= self.get_available_bandwith():
            self.signals.append(new_signal)
        else:
            print("Not enough bandwith available to add signal!")

    def print_signals_data(self):
        if self.signals:
            for signal in self.signals:
                print("Signal in channel:")
                print(signal.print_data() + '\n')
    
    def get_data(self):
        print(f'Location is {self.location}')
        print(f'Available bandwith is {self.get_available_bandwith()}')
        print('\n')
        self.print_signals_data()

test_signal_1 = Signal(location=(0, 0), bandwith_usage=5, is_incumbent = False)
test_signal_2 = Signal(location=(3, 5), bandwith_usage=10, is_incumbent = True)

test_channel = Channel(location=(1, 2), bandwith=50)

test_channel.add_signal(test_signal_1)
test_channel.add_signal(test_signal_2)

test_channel.get_data()



# Tkinter gui code below
root = Tk()
root.title("IEEE 802.22 Simulation")

mainframe = ttk.Frame(root, padding = "7 7 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

x_coord = DoubleVar()
x_coord_entry = ttk.Entry(mainframe, width=7, textvariable=x_coord)
x_coord_entry.grid(column=2, row=1, sticky=(W, E))

y_coord = DoubleVar()
y_coord_entry = ttk.Entry(mainframe, width=7, textvariable=y_coord)
y_coord_entry.grid(column=2, row=2, sticky=(W, E))

bandwith_gui = DoubleVar()
bandwith_entry = ttk.Entry(mainframe, width=7, textvariable=bandwith_gui)
bandwith_entry.grid(column=3, row=1, sticky=(W, E))

is_incumbent_gui = StringVar()
is_incumbent_entry = ttk.Entry(mainframe, width=7, textvariable=is_incumbent_gui)
is_incumbent_entry.grid(column=3, row=2, sticky=(W, E))

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)


root.mainloop()