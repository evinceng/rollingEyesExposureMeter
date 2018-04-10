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
        self.view.sidePanel.startButton.bind("<Button>",self.start)
        self.view.sidePanel.stopButton.bind("<Button>",self.stop)
        self.view.mainPanel.slider.bind("<B1-Motion>", self.read_bytes)
        self.view.mainPanel.progressbar["maximum"] = self.model.progressBarMaxVal
  
    def run(self):
        self.root.title("MVC")
        self.root.deiconify()
        self.root.mainloop()
         
    def start(self,event):
        self.view.sidePanel.startButton.config(state='disabled')
        self.view.sidePanel.stopButton.config(state='normal')
        self.clearSlider()

    def read_bytes(self,event):
        currentVal = self.view.mainPanel.slider.get()
        modelVal = self.model.start(currentVal)
        self.view.mainPanel.progressbar["value"] = modelVal
        
    def stop(self,event):
        self.view.sidePanel.startButton.config(state='normal')
        self.view.sidePanel.stopButton.config(state='disabled')
        self.clearSlider()
        self.model.stop()
        
    def clearSlider(self):
        self.view.mainPanel.progressbar["value"] = 0
        
        
  