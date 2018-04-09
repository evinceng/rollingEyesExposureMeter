# -*- coding: utf-8 -*-
"""
Created on Wed Apr 04 13:13:48 2018

@author: evin
"""
import Model
import View
import Tkinter as Tk
import matplotlib.animation as animation

class Controller():
    def __init__(self):
        self.root = Tk.Tk()
        self.model=Model.Model()
        self.view=View.View(self.root)
        self.view.sidepanel.plotBut.bind("<Button>",self.my_plot)
        self.view.sidepanel.clearButton.bind("<Button>",self.clear)
  
    def run(self):
        self.root.title("MVC")
        self.root.deiconify()
        self.root.mainloop()
         
    def clear(self,event):
        self.view.ax0.clear()
        self.view.fig.canvas.draw()
  
    def my_plot(self,event):
        self.model.calculate()
 #       ani = animation.FuncAnimation(self.view.fig, self.model.calculate(), interval=1000)
        self.view.ax0.clear()
        self.view.ax0.plot(self.model.xs,self.model.ys)
        self.view.fig.canvas.draw()