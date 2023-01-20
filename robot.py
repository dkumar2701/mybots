import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
class ROBOT:
    def __init__(self):
        self.robotID = p.loadURDF("body.urdf")
        
        
        
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for linkName, sensor in self.sensors.items():
            sensor.Get_Value(t)


    def Think(self):
        pass

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t):
        for motor in self.motors.values():
            motor.Set_Value(self.robotID, t)