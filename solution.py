import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = (numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons) *2) - 1
        self.myID = nextAvailableID

    def Set_ID(self, ID):
        self.myID = ID      
        
    def Start_Simulation(self, directOrGUI):
        if self.myID == 0:
            self.Create_World()
            self.Create_Body()
        self.Create_Brain()
        os.system("start /B python3 simulate.py " + directOrGUI + " " + str(self.myID) + " " )

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)
        
        f = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(f.read())
        f.close()
        #print("Fitness"+ str(self.myID)+": ", self.fitness, "\n")
        os.system("del fitness" + str(self.myID)+".txt")
        os.system("del array" + str(self.myID)+".txt")
        #print("Read: ", self.fitness)

    def Mutate(self):
        randomRow = random.randint(0, c.numSensorNeurons -1)
        randomColumn = random.randint(0, c.numMotorNeurons -1)
        self.weights[randomRow, randomColumn] = random.random() *2-1

    def Create_World(self):
        #Generate World
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[0, 1.5, 0.5] , size=[5, 1, 1])  
        pyrosim.End()

    def Create_Body(self):
        #Generate Robot
        legLength = 0.5
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1] , size=[1, 0.5, 0.5])  
        pyrosim.Send_Joint(name = "Torso_FrontLeft" , parent= "Torso" , child = "FrontLeft" , type = "revolute", 
            position = [0.25,0.25, 1 ], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeft", pos=[0, legLength/2, 0] , size=[0.2, legLength, 0.2])

        pyrosim.Send_Joint(name = "Torso_FrontRight" , parent= "Torso" , child = "FrontRight" , type = "revolute", 
            position = [-0.25,0.25, 1 ], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontRight", pos=[0, legLength/2, 0] , size=[0.2, legLength, 0.2])
        
        """
        
        pyrosim.Send_Joint(name = "BackLeg_BackLowerLeg", parent= "BackLeg", child= "BackLowerLeg", type= "revolute", position= [0, -1, 0],
            jointAxis= "1 0 0")
        pyrosim.Send_Cube(name= "BackLowerLeg", pos= [0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name = "BackLowerLeg_BackFoot", parent = "BackLowerLeg", child="BackFoot", type="revolute", position = [0, 0, -1], 
            jointAxis= "1 0 0")
        pyrosim.Send_Cube(name="BackFoot", pos= [0, 0, -0.1], size=[0.75, 0.75, 0.2])

        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0, 0.5, 1.2], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0] , size=[0.2,1,0.2]) 
        pyrosim.Send_Joint(name = "FrontLeg_FrontLowerLeg", parent= "FrontLeg", child= "FrontLowerLeg", type= "revolute", position= [0, 1, 0],
            jointAxis= "1 0 0")
        pyrosim.Send_Cube(name= "FrontLowerLeg", pos= [0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name = "FrontLowerLeg_FrontFoot", parent = "FrontLowerLeg", child="FrontFoot", type="revolute", position = [0, 0, -1], 
            jointAxis= "1 0 0")
        pyrosim.Send_Cube(name="FrontFoot", pos= [0, 0, -0.1], size=[0.75, 0.75, 0.2])

        pyrosim.Send_Joint(name="Torso_LeftLeg", parent= "Torso", child= "LeftLeg", type= "revolute", position= [-0.5, 0, 1.2], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name= "LeftLeg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name = "LeftLeg_LeftLowerLeg", parent= "LeftLeg", child= "LeftLowerLeg", type= "revolute", position= [-1, 0, 0],
            jointAxis= "0 1 0")
        pyrosim.Send_Cube(name= "LeftLowerLeg", pos= [0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name = "LeftLowerLeg_LeftFoot", parent = "LeftLowerLeg", child="LeftFoot", type="revolute", position = [0, 0, -1], 
            jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="LeftFoot", pos= [0, 0, -0.1], size=[0.75, 0.75, 0.2])

        pyrosim.Send_Joint(name = "Torso_RightLeg", parent= "Torso", child= "RightLeg", type= "revolute", position= [0.5, 0, 1.2], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name= "RightLeg", pos= [0.5, 0, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name = "RightLeg_RightLowerLeg", parent= "RightLeg", child= "RightLowerLeg", type= "revolute", position= [1, 0, 0],
            jointAxis= "0 1 0")
        pyrosim.Send_Cube(name= "RightLowerLeg", pos= [0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.Send_Joint(name = "RightLowerLeg_RightFoot", parent = "RightLowerLeg", child="RightFoot", type="revolute", position = [0, 0, -1], 
            jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="RightFoot", pos= [0, 0, -0.1], size=[0.75, 0.75, 0.2])
        """
        
        
        
        pyrosim.End()

    def Create_Brain(self):  
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        """
        
        pyrosim.Send_Sensor_Neuron(name = 0, linkName= "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1, linkName= "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2, linkName= "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 3, linkName= "LeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 4, linkName= "RightLeg")
        pyrosim.Send_Sensor_Neuron(name = 5, linkName= "BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 6, linkName= "FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 7, linkName= "LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 8, linkName= "RightLowerLeg")
        
        pyrosim.Send_Sensor_Neuron(name = 0, linkName= "BackFoot")
        pyrosim.Send_Sensor_Neuron(name = 1, linkName= "FrontFoot")
        pyrosim.Send_Sensor_Neuron(name = 2, linkName= "LeftFoot")
        pyrosim.Send_Sensor_Neuron(name = 3, linkName= "RightFoot")

        pyrosim.Send_Motor_Neuron(name = 4, jointName= "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name = 5, jointName= "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name = 6, jointName= "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name = 7, jointName= "Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name = 8, jointName= "BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron(name = 9, jointName= "FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron(name = 10, jointName= "LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron(name = 11, jointName= "RightLeg_RightLowerLeg")
        pyrosim.Send_Motor_Neuron(name = 12, jointName= "BackLowerLeg_BackFoot")
        pyrosim.Send_Motor_Neuron(name = 13, jointName= "FrontLowerLeg_FrontFoot")
        pyrosim.Send_Motor_Neuron(name = 14, jointName= "LeftLowerLeg_LeftFoot")
        pyrosim.Send_Motor_Neuron(name = 15, jointName= "RightLowerLeg_RightFoot")
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName= currentRow, targetNeuronName= currentColumn+c.numSensorNeurons, 
                    weight= self.weights[currentRow][currentColumn])
        """
        pyrosim.End()
        