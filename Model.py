# -*- coding: utf-8 -*-
"""
Created on Wed Apr 04 13:13:48 2018

@author: evin
"""

class Model():
 
    def __init__(self):  
        pass
    
    progressBarMaxVal = 2
    
    def start(self, slideVal):
        result = 2* slideVal**2
        print slideVal
        print result
        return result
    
    def stop(self):
        pass
         