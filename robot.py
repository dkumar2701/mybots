import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
class ROBOT:
    def __init__(self):
        self.robotID = p.loadURDF("body.urdf")
        
        self.motors = {}
        
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for linkName, sensor in self.sensors.items():
            sensor.Get_Value(t)