import numpy
import pyrosim.pyrosim as pyrosim
import constants as c
class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(c.totalStep)
        
    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        
        
    def Save_Values(self):
        numpy.save('data/'+self.linkName+'Sensor.npy', self.values)