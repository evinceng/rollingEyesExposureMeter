# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 16:05:35 2018

@author: evin
"""
import json
from bottle import response
import datetime
import time
import threading

class Sensor():
    
    __receivedEventCounterStr = "receivedEventCounter"

    receivedTobiiMessage=[]
    receivedTobiiMessage.append(json.loads('{"tobiiEyeTracker":{"timeStamp":"30.12.2015 14:06:20.2412","leftPos":{"x":"-0,228793755914194","y":"11,5027813555582","z":"60,912982163767"},"rightPos":{"x":"5,89524352818696","y":"11,2245013358383","z":"61,0730322352786"},"leftGaze":{"x":"3,15812377150551","y":"17,3247499470179","z":"4,61986983600664"},"rightGaze":{"x":"-2,49937069615642","y":"17,3932511520527","z":"4,64480229580618"},"leftPupilDiameter":"2,645874","rightPupilDiameter":"2,622345"}}'))
    receivedTobiiMessage.append(json.loads('{"tobiiEyeTracker":{"timeStamp":"30.12.2015 14:06:20.2442","leftPos":{"x":"-0,258863875351471","y":"11,5149518687205","z":"60,9095247803002"},"rightPos":{"x":"5,88168331298095","y":"11,2362714331765","z":"61,0613078775579"},"leftGaze":{"x":"2,38144559635971","y":"16,7283881083418","z":"4,40281135417063"},"rightGaze":{"x":"-3,55454772939922","y":"17,2529816540119","z":"4,59374825056375"},"leftPupilDiameter":"2,642151","rightPupilDiameter":"2,673187"}}'))
    
    def __init__(self, configSectionName):
        __timeStamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H%M%S')
        self.configSectionName = configSectionName
        self.logFileName = configSectionName + "Log_" + __timeStamp + ".log"
        self.keepListeningCond = threading.Condition()
        self.halt = 0
        self.__receivedEventCounter = 1
        
    def listenSocketFromDotNET(self):
        self.halt = 0
        while 1:
            with self.keepListeningCond:
                if not self.halt:
                    print "current time is ", time.strftime("%H:%M:%S")
                    time.sleep(2)
                else:
                    break
        print "Leaving listening method of ", self.configSectionName
    
    def respondTracker(self):
        response.headers["Content-type"] = "application/json"
        data = {}
        
        self.__receivedEventCounter = self.__receivedEventCounter + 1
        
        data[self.__receivedEventCounterStr] = self.__receivedEventCounter        
        data[self.logFileName] = self.receivedTobiiMessage
        json_data = json.dumps(data)
        
        return json_data
    
    def stop(self):
        with self.keepListeningCond:
            self.halt = 1
            self.keepListeningCond.notify() #All()