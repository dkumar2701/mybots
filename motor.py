import constants as c
import pyrosim.pyrosim as pyrosim
import numpy
class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.amplitudeBackLeg
        self.frequency = c.frequencyBackLeg
        self.offset = c.phaseOffsetBackLeg
        self.motorValues = numpy.sin(self.frequency*c.x + self.offset) * self.amplitude
        #pyrosim.Set_Motor_For_Joint(
        #bodyIndex = robotID,
        #jointName = "Torso_BackLeg",
        #controlMode = p.POSITION_CONTROL,
        #targetPosition = -c.targetAnglesBackLeg[i], 
        #maxForce = 75)
        #pyrosim.Set_Motor_For_Joint(
        #bodyIndex = robotID,
        #jointName = "Torso_FrontLeg",
        #controlMode = p.POSITION_CONTROL,
        #targetPosition = -c.targetAnglesFrontLeg[i], 
        #maxForce = 75)