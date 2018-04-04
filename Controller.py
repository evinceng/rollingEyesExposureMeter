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
        self.view.sidepanel.plotBut.bind("<Button>",self.my_plot)
        self.view.sidepanel.clearButton.bind("<Button>",self.clear)
  
    def run(self):
        self.root.title("Tkinter MVC example")
        self.root.deiconify()
        self.root.mainloop()
         
    def clear(self,event):
        self.view.ax0.clear()
        self.view.fig.canvas.draw()
  
    def my_plot(self,event):
        self.model.calculate()
        self.view.ax0.clear()
        self.view.ax0.contourf(self.model.res["x"],self.model.res["y"],self.model.res["z"])
        self.view.fig.canvas.draw()