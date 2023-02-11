import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.blockNum = random.randint(c.minlen, c.maxlen)
        self.sensorTrue = numpy.random.randint(0, 2, size=self.blockNum)
        self.numSensorNeurons = numpy.sum(self.sensorTrue)
        self.numMotorNeurons = self.blockNum - 1
        self.weights = (numpy.random.rand(self.numSensorNeurons,self.numMotorNeurons) *2) - 1
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
        #pyrosim.Send_Cube(name="Box", pos=[0, 2, 0.25] , size=[10, 1, 0.5], mass=1000000)
        #pyrosim.Send_Cube(name="Box", pos=[0, 3, 0.5] , size=[5, 1, 1], mass=1000)  
        pyrosim.End()

    def Determine_Color(self, i):
        if self.sensorTrue[i] == 1:
            return "Green"
        else:
            return "Cyan"

    def Create_Body(self):
        #Generate Robot
        zdiff = c.maxdim/2
        
        jointDir = ["1 0 0", "0 1 0", "0 0 1"]
        print("The Sensors: ", self.sensorTrue, "\n")

        pyrosim.Start_URDF("body.urdf")
        #Create connecting blocks
        
        for i in range(self.blockNum):
            xsize = random.uniform(c.mindim, c.maxdim)
            ysize = random.uniform(c.mindim, c.maxdim)
            zsize = random.uniform(c.mindim, c.maxdim)
            if i == 0:
                blockpos = [0, 0, zdiff]
            else:
                blockpos = [0, -ysize/2, 0]
            pyrosim.Send_Cube(name= str(i), pos=blockpos , size=[xsize, ysize , zsize], color = self.Determine_Color(i))

            #lastSize = [xsize, ysize, zsize]
                
            
            #Create joints if we are not in the last block (all revolute and X axis)
            if i < self.blockNum-1:
                thisAxisidx = random.randint(0,2)
                if i==0:
                    jointPos = [0, -ysize/2, zdiff]
                else:
                    jointPos = [0, -ysize, 0]
                pyrosim.Send_Joint(name = str(i) + "_" + str(i+1), parent= str(i), child= str(i+1),
                                       type="revolute", position= jointPos, jointAxis= jointDir[thisAxisidx])
                    
        

          
    
        #pyrosim.Send_Joint(name = "Torso_FrontLeft" , parent= "Torso" , child = "FrontLeft" , type = "revolute", 
         #   position = [-0.25, -1+(width/2 - 0.1), legLength ], jointAxis = "0 1 0")
        
        pyrosim.End()

    def Create_Brain(self):  
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        
        
        for i in range(self.blockNum):
            if self.sensorTrue[i]:
                pyrosim.Send_Sensor_Neuron(name = i, linkname = str(i))
                numSensorNeurons+= 1
            if i < self.blockNum - 1:
                pyrosim.Send_Motor_Neuron(name = )
            
        #pyrosim.Send_Sensor_Neuron(name = 5, linkName= "RightLower")
        

        #pyrosim.Send_Motor_Neuron(name = 16, jointName= "Torso_Right")
        #pyrosim.Send_Motor_Neuron(name = 17, jointName= "Right_RightLower")
        """
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName= currentRow, targetNeuronName= currentColumn+c.numSensorNeurons, 
                    weight= self.weights[currentRow][currentColumn])
        """
        pyrosim.End()
        