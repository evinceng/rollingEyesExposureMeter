# -*- coding: utf-8 -*-
"""
Created on Wed Apr 04 13:12:21 2018

@author: evin
"""

import Tkinter as Tk

class View():
    def __init__(self, master):
        self.frame = Tk.Frame(master)
        self.frame.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)
        self.sidepanel=SidePanel(master)
 
class SidePanel():
    def __init__(self, root):
        self.frame2 = Tk.Frame( root )
        self.frame2.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)
        self.startBut = Tk.Button(self.frame2, text="Start ")
        self.startBut.pack(side="top",fill=Tk.BOTH)
        self.stopButton = Tk.Button(self.frame2, text="Stop")
        self.stopButton.pack(side="top",fill=Tk.BOTH)
