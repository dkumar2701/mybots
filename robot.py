import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c
import numpy as np

class ROBOT:
    def __init__(self, solutionID):
        self.robotID = p.loadURDF("body" + solutionID + ".urdf")
        self.nn = NEURAL_NETWORK("brain" + solutionID + ".nndf")
        os.system("del brain" + solutionID + ".nndf")
        
        
        
    def Prepare_To_Sense(self):
        self.sensors = {}
        self.zPositions = np.zeros(c.totalStep)
        
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for linkName, sensor in self.sensors.items():
            sensor.Get_Value(t)
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotID)
        basePosition = basePositionAndOrientation[0]
        self.zPositions[t] = basePosition[2]


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
        yPosition = basePosition[1]
        zPosition = basePosition[2]
        xPosition = basePosition[0]
        #For jumping
        """
        sensorVals = {}
        sensorVals["BackFoot"] = self.sensors["BackFoot"].values
        sensorVals["FrontFoot"] = self.sensors["FrontFoot"].values
        sensorVals["LeftFoot"] = self.sensors["LeftFoot"].values
        sensorVals["RightFoot"] = self.sensors["RightFoot"].values
        #meanLegs = {}
        sensorBigArray =  np.zeros((0, sensorVals["BackFoot"].shape[0]))
        for key, value in sensorVals.items():
            sensorBigArray = np.vstack((sensorBigArray, value))
        meanArray = np.mean(sensorBigArray, axis = 0)
        #print("meanArray: ", meanArray, "\n")
        airTime = 0
        currairTime = 0
        contiguous=False
        for i in range(c.totalStep):
            if meanArray[i] == -1:
                currairTime += 1
                if contiguous == False:
                    contiguous = True
            elif meanArray[i] != -1 & contiguous:
                contiguous = False
                if currairTime > airTime:
                    airTime = currairTime
                currairTime = 0
        """
        #All negative -1 means mean across all is -1
        #print("Airtime: ", airTime, "\n")
        #print(xCoordinateOfLinkZero)
        #print("Zposns: ", self.zPositions, "\n")
        maxZ = np.max(self.zPositions)
        
        fitness = yPosition
        f = open("tmp" + solutionID + ".txt", "w")
        f.write(str(fitness))
        f.close()
        os.rename("tmp"+str(solutionID)+".txt" , "fitness"+str(solutionID)+".txt")
        """
        f = open("arraytmp"+ solutionID + ".txt", "w")
        f.write(str(meanArray))
        f.close()
        os.rename("arraytmp"+str(solutionID)+".txt" , "array"+str(solutionID)+".txt")
        """
        
                