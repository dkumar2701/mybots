import constants as c
import pyrosim.pyrosim as pyrosim
import numpy
import pybullet as p
class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.amplitudeBackLeg
        if self.jointName == "Torso_BackLeg":
            self.frequency = c.frequencyBackLeg/2
        else:
            self.frequency = c.frequencyBackLeg
        self.offset = c.phaseOffsetBackLeg
        self.motorValues = numpy.sin(self.frequency*c.x + self.offset) * self.amplitude
        
    
    def Set_Value(self, robotID, t):
        pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotID,
        jointName = self.jointName,
        controlMode = p.POSITION_CONTROL,
        targetPosition = self.motorValues[t], 
        maxForce = 25)
        