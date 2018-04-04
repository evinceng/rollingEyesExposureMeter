# -*- coding: utf-8 -*-
"""
Created on Wed Apr 04 13:12:21 2018

@author: evin
"""

import Tkinter as Tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class View():
    def __init__(self, master):
        self.frame = Tk.Frame(master)
        self.fig = Figure( figsize=(7.5, 4), dpi=80 )
        self.ax0 = self.fig.add_axes( (0.05, .05, .90, .90), axisbg=(.75,.75,.75), frameon=False)
        self.frame.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)
        self.sidepanel=SidePanel(master)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        self.canvas.show()
 
class SidePanel():
    def __init__(self, root):
        self.frame2 = Tk.Frame( root )
        self.frame2.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)
        self.plotBut = Tk.Button(self.frame2, text="Plot ")
        self.plotBut.pack(side="top",fill=Tk.BOTH)
        self.clearButton = Tk.Button(self.frame2, text="Clear")
        self.clearButton.pack(side="top",fill=Tk.BOTH)