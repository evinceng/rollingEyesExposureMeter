# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 15:57:39 2018

@author: evin
"""

import threading

class ThreadedSensor():
    
    def __init__(self, sensor, configSectionName):
        self.sensor = sensor
        self.configSectionName = configSectionName
    
    def startListening(self):
        print self.configSectionName, " started listening"
        
        self.listeningSensorSocketThread = threading.Thread(target=self.sensor.listenSocketFromDotNET , args=())
        self.listeningSensorSocketThread.start()
        
    def stopListening(self):
        print self.configSectionName, " stopped listening"
        self.sensor.stop()