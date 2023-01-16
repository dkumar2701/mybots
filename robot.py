import pybullet as p
import pyrosim.pyrosim as pyrosim
class ROBOT:
    def __init__(self):
        self.robotID = p.loadURDF("body.urdf")
        
        self.motors = {}
        
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            print(linkName)