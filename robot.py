import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c

class ROBOT:
    def __init__(self, solutionID):
        self.robotID = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain" + solutionID + ".nndf")
        os.system("del brain" + solutionID + ".nndf")
        
        
        
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for linkName, sensor in self.sensors.items():
            sensor.Get_Value(t)


    def Think(self):
        self.nn.Update()
        #self.nn.Print()
       

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(self.robotID, desiredAngle)

    def Get_Fitness(self, solutionID):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotID)
        basePosition = basePositionAndOrientation[0]
        yPosition = basePosition[2]
        #print(xCoordinateOfLinkZero)
        f = open("tmp" + solutionID + ".txt", "w")
        f.write(str(yPosition))
        f.close()
        os.rename("tmp"+str(solutionID)+".txt" , "fitness"+str(solutionID)+".txt")
        
                