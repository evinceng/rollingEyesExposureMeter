# -*- coding: utf-8 -*-
"""
Created on Wed Apr 04 12:31:46 2018

@author: evin
"""
import Controller
import ConfigParser

__configFileName = "config.ini"

if __name__ == "__main__":
    config = ConfigParser.ConfigParser()
    config.read(__configFileName)
    c = Controller.Controller(config)
    c.run()
    
    