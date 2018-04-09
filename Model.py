# -*- coding: utf-8 -*-
"""
Created on Wed Apr 04 13:13:48 2018

@author: evin
"""
import time
from random import randint
import collections

class Model():
 
    def __init__(self):
        self.xs=collections.deque(5*[0], 5)
        self.ys=collections.deque(5*[0], 5)
  
  
    def calculate(self):
        self.xs.append(time.strftime("%H:%M:%S"))
        self.ys.append(randint(0,10))
        