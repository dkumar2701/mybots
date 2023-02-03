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
        pyrosim.Send_Cube(name="Box", pos=[0, 2, 0.25] , size=[100, 1, 0.5], mass=1000000)
        #pyrosim.Send_Cube(name="Box", pos=[0, 3, 0.5] , size=[5, 1, 1], mass=1000)  
        pyrosim.End()

    def Create_Body(self):
        #Generate Robot
        legLength = 0.75
        width = 2
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, legLength] , size=[width, 0.5, 0.5])  
        pyrosim.Send_Joint(name = "Torso_FrontLeft" , parent= "Torso" , child = "FrontLeft" , type = "revolute", 
            position = [-(width/2 - 0.5), 0.25, legLength ], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeft", pos=[0, legLength/2, 0] , size=[0.2, legLength, 0.2])
        pyrosim.Send_Joint(name = "FrontLeft_FLLower" , parent= "FrontLeft" , child = "FLLower" , type = "revolute", 
            position = [0, legLength, 0 ], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FLLower", pos=[0, 0, -legLength/2] , size=[0.2, 0.2, legLength])
        
        pyrosim.Send_Joint(name = "Torso_FrontRight" , parent= "Torso" , child = "FrontRight" , type = "revolute", 
            position = [(width/2 - 0.5),0.25, legLength ], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontRight", pos=[0, legLength/2, 0] , size=[0.2, legLength, 0.2])
        pyrosim.Send_Joint(name = "FrontRight_FRLower" , parent= "FrontRight" , child = "FRLower" , type = "revolute", 
            position = [0, legLength, 0 ], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FRLower", pos=[0, 0, -legLength/2] , size=[0.2, 0.2, legLength])
        
        pyrosim.Send_Joint(name = "Torso_BackLeft" , parent= "Torso" , child = "BackLeft" , type = "revolute", 
            position = [-(width/2 - 0.5),-0.25, legLength ], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeft", pos=[0, -legLength/2, 0] , size=[0.2, legLength, 0.2])
        pyrosim.Send_Joint(name = "BackLeft_BLLower" , parent= "BackLeft" , child = "BLLower" , type = "revolute", 
            position = [0, -legLength, 0 ], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BLLower", pos=[0, 0, -legLength/2] , size=[0.2, 0.2, legLength])

        pyrosim.Send_Joint(name = "Torso_BackRight" , parent= "Torso" , child = "BackRight" , type = "revolute", 
            position = [(width/2 - 0.5),-0.25, legLength ], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackRight", pos=[0, -legLength/2, 0] , size=[0.2, legLength, 0.2])
        pyrosim.Send_Joint(name = "BackRight_BRLower" , parent= "BackRight" , child = "BRLower" , type = "revolute", 
            position = [0, -legLength, 0 ], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BRLower", pos=[0, 0, -legLength/2] , size=[0.2, 0.2, legLength])

        pyrosim.Send_Joint(name = "Torso_Left" , parent= "Torso" , child = "Left" , type = "revolute", 
            position = [-(width/2), 0, legLength ], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="Left", pos=[-legLength/2, 0, 0] , size=[legLength, 0.2, 0.2])
        pyrosim.Send_Joint(name = "Left_LeftLower" , parent= "Left" , child = "LeftLower" , type = "revolute", 
            position = [-legLength, 0, 0 ], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="LeftLower", pos=[0, 0, -legLength/2] , size=[0.2, 0.2, legLength])

        pyrosim.Send_Joint(name = "Torso_Right" , parent= "Torso" , child = "Right" , type = "revolute", 
            position = [width/2, 0, legLength ], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="Right", pos=[legLength/2, 0, 0] , size=[legLength, 0.2, 0.2])
        pyrosim.Send_Joint(name = "Right_RightLower" , parent= "Right" , child = "RightLower" , type = "revolute", 
            position = [legLength, 0, 0 ], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="RightLower", pos=[0, 0, -legLength/2] , size=[0.2, 0.2, legLength])
        
        
        
        pyrosim.End()

    def Create_Brain(self):  
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        
        pyrosim.Send_Sensor_Neuron(name = 0, linkName= "FLLower")
        pyrosim.Send_Sensor_Neuron(name = 1, linkName= "FRLower")
        pyrosim.Send_Sensor_Neuron(name = 2, linkName= "BLLower")
        pyrosim.Send_Sensor_Neuron(name = 3, linkName= "BRLower")
        pyrosim.Send_Sensor_Neuron(name = 4, linkName= "LeftLower")
        pyrosim.Send_Sensor_Neuron(name = 5, linkName= "RightLower")
        

        pyrosim.Send_Motor_Neuron(name = 6, jointName= "Torso_FrontLeft")
        pyrosim.Send_Motor_Neuron(name = 7, jointName= "Torso_FrontRight")
        pyrosim.Send_Motor_Neuron(name = 8, jointName= "Torso_BackLeft")
        pyrosim.Send_Motor_Neuron(name = 9, jointName= "Torso_BackRight")
        pyrosim.Send_Motor_Neuron(name = 10, jointName= "FrontLeft_FLLower")
        pyrosim.Send_Motor_Neuron(name = 11, jointName= "FrontRight_FRLower")
        pyrosim.Send_Motor_Neuron(name = 12, jointName= "BackLeft_BLLower")
        pyrosim.Send_Motor_Neuron(name = 13, jointName= "BackRight_BRLower")
        pyrosim.Send_Motor_Neuron(name = 14, jointName= "Torso_Left")
        pyrosim.Send_Motor_Neuron(name = 15, jointName= "Left_LeftLower")
        pyrosim.Send_Motor_Neuron(name = 16, jointName= "Torso_Right")
        pyrosim.Send_Motor_Neuron(name = 17, jointName= "Right_RightLower")
        
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName= currentRow, targetNeuronName= currentColumn+c.numSensorNeurons, 
                    weight= self.weights[currentRow][currentColumn])
                    
        pyrosim.End()
        