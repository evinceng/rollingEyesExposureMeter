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
import socket
import config
import sys

class Sensor():
    
    sensorMessage=[]
    #sensorMessage.append(json.loads('{"tobiiEyeTracker":{"timeStamp":"30.12.2015 14:06:20.2412","leftPos":{"x":"-0,228793755914194","y":"11,5027813555582","z":"60,912982163767"},"rightPos":{"x":"5,89524352818696","y":"11,2245013358383","z":"61,0730322352786"},"leftGaze":{"x":"3,15812377150551","y":"17,3247499470179","z":"4,61986983600664"},"rightGaze":{"x":"-2,49937069615642","y":"17,3932511520527","z":"4,64480229580618"},"leftPupilDiameter":"2,645874","rightPupilDiameter":"2,622345"}}'))
    #sensorMessage.append(json.loads('{"tobiiEyeTracker":{"timeStamp":"30.12.2015 14:06:20.2442","leftPos":{"x":"-0,258863875351471","y":"11,5149518687205","z":"60,9095247803002"},"rightPos":{"x":"5,88168331298095","y":"11,2362714331765","z":"61,0613078775579"},"leftGaze":{"x":"2,38144559635971","y":"16,7283881083418","z":"4,40281135417063"},"rightGaze":{"x":"-3,55454772939922","y":"17,2529816540119","z":"4,59374825056375"},"leftPupilDiameter":"2,642151","rightPupilDiameter":"2,673187"}}'))
    
    def __init__(self, configSectionName):
        __timeStamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H%M%S')
        self.configSectionName = configSectionName
        self.logFileName = configSectionName + "Log_" + __timeStamp + ".log"
        self.keepListeningCond = threading.Condition()
        self.halt = 0
        self.__receivedEventCounter = 0
        
    
    def listenSocketFromDotNET(self):
        self.halt = 0
        self.sock = self.__initSocket()
        
        try:
            while True:
#                print "current time is ", time.strftime("%H:%M:%S")
                # Wait for a connection
                print >>sys.stderr, "Server socket for incomming ", self.configSectionName, " data: waiting for a connection"
                connection, client_address = self.sock.accept()
                
                if not self.halt:
                    try:
                        while True:
                            if not self.halt:
                                print >>sys.stderr, "Server socket for incomming ", self.configSectionName, " data: connection from", client_address
                                self.__receivedEventCounter = self.__receivedEventCounter + 1
                                data = connection.recv(10000) # kinda ugly hack. If incomming message will be longer this will spill.
                            
                                if config.getConfig().getboolean(self.configSectionName, "IsDataHasToBeParsed"):
                                    __parsedData = self.parseData(self, data)
                                    data = __parsedData
                                self.sensorMessage.append(json.loads(data))
                                self.__writeToFile(data, "a")
                            
                                if data:
                                    print >>sys.stderr, "Server socket for incomming ", self.configSectionName, " data: sending data back to the client"
                                    connection.sendall(data)
                                else:
                                    print >>sys.stderr, "Server socket for incomming ", self.configSectionName, " data: no more data from", client_address
                                    break
                            else:
                                break
                    except Exception as e:
                        print("something's wrong with %s. Exception is %s" % (client_address, e))
                    finally:
                        # Clean up the connection
                        connection.shutdown(1)
                        connection.close()
                        print "Closing incomming ", self.configSectionName, " data socket connection."
                else:
                    break
        finally: 
            self.sock.close()
            print "Finished server socket for incomming ", self.configSectionName, " data thread"
                     
        print "Leaving listening method of ", self.configSectionName
    
    def respondTracker(self):
        response.headers["Content-type"] = "application/json"
        data = {}
        
        data["receivedEventCounter"] = self.__receivedEventCounter        
        data[self.logFileName] = self.sensorMessage
        json_data = json.dumps(data)
        self.sensorMessage = []
        return json_data
    
    def stop(self):
        """
        halt flag is set and one last connect made locally
        in order get listen method out of loop 
        """
        self.halt = 1
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (config.getConfig().get(self.configSectionName, "Url"), config.getConfig().getint(self.configSectionName, "Port"))
        sock.connect(server_address)
        sock.close()
        
    def __initSocket(self):
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bind the socket to the port
        server_address = (config.getConfig().get(self.configSectionName, "Url"), config.getConfig().getint(self.configSectionName, "Port"))    
        print >>sys.stderr, "Server socket for incomming ", self.configSectionName, " data: starting up on %s port %s" % server_address
        sock.bind(server_address)   
        # Listen for incoming connections
        sock.listen(1)
        return sock
    
    def __writeToFile(self, data, mode):
        """ 
        Opens the file named sectionName+LocalLoggingFileName in the specified @mode and writes the
        @data to it and closes the file.
    
        @param data (string): The data that will be written to the file
        @param mode (char): The mode to open the file
        """
        try:
            f = open(self.logFileName, mode)                        
            f.write(data)
        except IOError:
            print("Error while writing to file: ")
        finally:
            f.close()
            
    def parseData(self, data):
        if config.getConfig().getboolean(self.configSectionName, "IsDataHasToBeParsed"):
            raise NotImplementedError("It seems that the data has to be parsed. Please override and implement parseData method!")
        else:
            raise NotImplementedError("It is declared that the data don\'t need to be parsed. Please check config file!")
            