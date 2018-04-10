# -*- coding: utf-8 -*-
"""
Created on Wed Apr 04 13:13:48 2018

@author: evin
"""

class Model():
    """ Class including the main operations of the app.
        (Model of MVC)
    """
    def __init__(self):  
        pass
    
    progressBarMaxVal = 2
    """Progress Bar's max value """
    
    def start(self, slideVal):
        result = 2* slideVal**2
        print slideVal
        print result
        return result
    
    def stop(self):
        pass
         