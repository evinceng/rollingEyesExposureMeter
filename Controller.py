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
#        self.view.mainpanel.start_button.bind("<Button>", self.start)
        self.view.sidepanel.startBut.bind("<Button>",self.start)
        self.view.sidepanel.stopButton.bind("<Button>",self.stop)
        self.currentVal = 0
        self.maxVal = 100
  
    def run(self):
        self.root.title("MVC")
        self.root.deiconify()
        self.root.mainloop()
         
    def start(self,event):
        self.view.mainpanel.progressbar["value"] = 0
        self.view.mainpanel.progressbar["maximum"] = self.maxVal
        self.read_bytes()

    def read_bytes(self):
        self.currentVal = self.model.start()
        self.view.mainpanel.progressbar["value"] = self.currentVal
        self.view.mainpanel.progressbar.after(100, self.read_bytes)
        
    def stop(self,event):
        self.model.stop()
  