
"""
This object will read data(which was written by ios), and write data(flask's jsonread)
"""
import json

class bleObject:
    def __init__(self): #Read readfile and write it to writefile since last changes are in readfile
        with open('myjsonRead.json', 'r') as read_file:
            dataread = json.load(read_file)
        with open('myjsonWrite.json', 'w') as write_file:
            json.dump(dataread, write_file)
        self.lastvaluesseen = dataread 
        
    def print(self): #prints last values sent to ble's READ METHOD
        print("BLEOBJECT has this values: ", self.lastvaluesseen)

    def writerhas(self): #reads myjsonwrite file
        with open("myjsonWrite.json", "r") as read_file:
            dataread = json.load(read_file)
        return dataread
    
    def writeTV(self, mybool): #writes myjsonRead file change in tv
        if mybool:
            self.lastvaluesseen["TVmotor"] = 1
        else:
            self.lastvaluesseen["TVmotor"] = 0
        with open('myjsonRead.json', 'w') as write_file:
            json.dump(self.lastvaluesseen, write_file)
        print("We have written the change in TV.")  


     
    def comparechanges(self): # compares the values written by IOS with last values written to FLASK
         pass
