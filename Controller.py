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
        self.view.mainpanel.slider.bind("<B1-Motion>", self.read_bytes)
        self.view.mainpanel.progressbar["maximum"] = 2
  
    def run(self):
        self.root.title("MVC")
        self.root.deiconify()
        self.root.mainloop()
         
    def start(self,event):
        self.clearSlider()

    def read_bytes(self,event):
        currentVal = self.view.mainpanel.slider.get()
        modelVal = self.model.start(currentVal)
        self.view.mainpanel.progressbar["value"] = modelVal
        
    def stop(self,event):
        self.model.stop()
        self.clearSlider()
        
    def clearSlider(self):
        self.view.mainpanel.progressbar["value"] = 0
        
        
  