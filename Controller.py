# -*- coding: utf-8 -*-
"""
Created on Wed Apr 04 13:13:48 2018

@author: evin
"""
import Model
import View
import Tkinter as Tk

class Controller():
    def __init__(self):
        self.root = Tk.Tk()
        self.model=Model.Model()
        self.view=View.View(self.root)
        self.view.sidepanel.startBut.bind("<Button>",self.start)
        self.view.sidepanel.stopButton.bind("<Button>",self.stop)
  
    def run(self):
        self.root.title("MVC")
        self.root.deiconify()
        self.root.mainloop()
         
    def stop(self,event):
        pass
  
    def start(self,event):
        self.model.start()