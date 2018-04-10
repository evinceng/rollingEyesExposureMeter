# -*- coding: utf-8 -*-
"""
Created on Wed Apr 04 13:13:48 2018

@author: evin
"""
import Model
import View
import Tkinter as Tk

class Controller():
    """Class establishing communication between user interface(view) and model.
       (Controller of MVC)
    """
    def __init__(self):
        self.root = Tk.Tk()
        self.model=Model.Model()
        self.view=View.View(self.root)
        self.view.sidePanel.startButton.bind("<Button>",self.start)
        self.view.sidePanel.stopButton.bind("<Button>",self.stop)
        #first benchmark commented out
#        self.view.mainPanel.slider.bind("<B1-Motion>", self.calculateVal)
#        self.view.mainPanel.progressbar["maximum"] = self.model.progressBarMaxVal
  
    def run(self):
        self.root.title("MVC")
        self.root.deiconify()
        self.root.mainloop()
        
    def start(self,event):
        self.view.sidePanel.startButton.config(state="disabled")
        self.view.sidePanel.stopButton.config(state="normal")
        #first benchmark commented out
#        self.clearSlider()
        
    def stop(self,event):
        self.view.sidePanel.startButton.config(state="normal")
        self.view.sidePanel.stopButton.config(state="disabled")
        #first benchmark commented out
#        self.clearSlider()
        self.model.stop()
        
#first benchmark commented out
#    def calculateVal(self,event):
#        currentVal = self.view.mainPanel.slider.get()
#        modelVal = self.model.start(currentVal)
#        self.view.mainPanel.progressbar["value"] = modelVal
#        
#    def clearSlider(self):
#        self.view.mainPanel.progressbar["value"] = self.model.progressBarMinVal
        
        
  