import numpy
import pyrosim.pyrosim as pyrosim
import os
import time
import constants as c
from node import NODE 
import math

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.blockNum = numpy.random.randint(c.minlen, c.maxlen+1)
        if(nextAvailableID < c.populationSize):
            print("Number of nodes", str(nextAvailableID), ": ", self.blockNum, "\n")
        self.sensorTrue = numpy.random.randint(0, 2, size=self.blockNum)
        self.numSensorNeurons = 0
        self.nodeList = list(range(self.blockNum))
        self.ID_node = {}
        self.lastRemoved = -1
        #Add nodes to the nodeList
        for i in range(self.blockNum):
            currentNode = NODE(i)
            if currentNode.isSensor == 1:
                self.numSensorNeurons += 1
            self.nodeList[i] = currentNode
            self.ID_node[i] = currentNode
        if self.numSensorNeurons == 0:
            oneSensor = numpy.random.randint(0, self.blockNum)
            sensorNode = self.nodeList[oneSensor]
            sensorNode.isSensor = 1
            self.numSensorNeurons = 1
        self.numMotorNeurons = self.blockNum - 1
        self.weights = (numpy.random.rand(self.numSensorNeurons,self.numMotorNeurons) *2) - 1
        self.myID = nextAvailableID
        self.availableBlocks = list(range(1)) #create a list of the available block IDS
        self.removedfromAvailable = []
        #Create the connections:
        self.Add_Connections()
        self.initialZ = 2


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
        while True:
            try:
                f = open("fitness" + str(self.myID) + ".txt", "r")
                break
            except:
                pass
        self.fitness = float(f.read())
        f.close()
        #print("Fitness"+ str(self.myID)+": ", self.fitness, "\n")
        os.system("del fitness" + str(self.myID)+".txt")
        os.system("del array" + str(self.myID)+".txt")
        #print("Read: ", self.fitness)

    def Mutate(self):
        #Add/Remove another block
        #self.AddNewNode()
        addOrRemove = numpy.random.randint(0, 2)
        if self.numSensorNeurons == 1:
            self.AddNewNode()
        elif self.blockNum > 3 and self.blockNum < c.maxlen + 3:
            if addOrRemove == 1:
                self.DeleteNode()
            else:
                self.AddNewNode()
        elif self.blockNum <= 3:
            self.AddNewNode()
        elif self.blockNum >= c.maxlen + 3:
            self.DeleteNode()
        randomRow = numpy.random.randint(0, self.numSensorNeurons)
        randomColumn = numpy.random.randint(0, self.numMotorNeurons)
        self.weights[randomRow, randomColumn] = numpy.random.random() *2-1
        
    def DeleteNode(self):
        #Remove new node
        #print("DELETING A NODE\n")
        removedNode = self.nodeList.pop()
        self.ID_node.pop(self.blockNum - 1)
        #remove column of size numSensors for the new motor neuron
        self.weights = numpy.delete(self.weights, self.numMotorNeurons - 1, 1)
        self.numMotorNeurons -= 1
        if (removedNode.isSensor):
            self.weights = numpy.delete(self.weights, self.numSensorNeurons -1, 0)
            self.numSensorNeurons -= 1
        #Remove connections
        removedNode.disconnect()
        self.availableBlocks.remove(removedNode.ID)
        if removedNode.previousNode.full == False and removedNode.previousNode.ID not in self.availableBlocks:
            self.availableBlocks.append(removedNode.previousNode.ID)
        if len(self.availableBlocks) < 4 and self.lastRemoved != -1:
            if self.lastRemoved != removedNode.ID:
                self.availableBlocks.append(self.lastRemoved)
            else:
                newlist = self.removedfromAvailable
                newlist.remove(removedNode.ID)
                self.availableBlocks.append(numpy.random.choice(newlist))
        self.blockNum -=1

    def AddNewNode(self):
        #creating new node
        #print("ADDING A NODE\n")
        newNode = NODE(self.blockNum)
        self.nodeList.append(newNode)
        self.ID_node[self.blockNum] = newNode
        self.numMotorNeurons += 1
        #add new column of size numSensors for the new motor neuron
        newcol = (numpy.random.rand(self.numSensorNeurons, 1) *2) -1
        self.weights = numpy.hstack((self.weights, newcol))
        if (newNode.isSensor):
            self.numSensorNeurons += 1
            newrow = (numpy.random.rand(1, self.numMotorNeurons) *2) -1
            self.weights = numpy.vstack((self.weights, newrow))
        #add connections
        newNodetoConnect = self.nodeList[self.connect_TO()]
        newNode.connect(newNodetoConnect)
        self.availableBlocks.append(newNode.ID)
        if newNodetoConnect.full:
            self.availableBlocks.remove(newNodetoConnect.ID)
        if len(self.availableBlocks) ==5:
            self.lastRemoved = self.availableBlocks.pop(0)
            self.removedfromAvailable.append(self.lastRemoved)
        self.blockNum +=1



        

    def Create_World(self):
        #Generate World
        pyrosim.Start_SDF("world.sdf")
        #pyrosim.Send_Cube(name="Box", pos=[0, 2, 0.25] , size=[10, 1, 0.5], mass=1000000)
        #pyrosim.Send_Cube(name="Box", pos=[0, 3, 0.5] , size=[5, 1, 1], mass=1000)  
        pyrosim.End()

    def Determine_Color(self, node):
        if node.isSensor == 1:
            return "Green"
        else:
            return "Cyan"

    #Decide which node to connect to based on the available options
    def connect_TO(self):
        numOptions = len(self.availableBlocks)
        #optionList = list(range(numOptions))
        weightlist = []
        #Prefer to add to the last chained block (when node prefers any direction, this becomes the root block)
        for i in range(numOptions):
            if self.ID_node[self.availableBlocks[i]].lastChain:
                weightlist.append(c.preferLastChain)
            else:
                weightlist.append(1)
        p = numpy.array(weightlist)/sum(weightlist)
        nodeIDtoConnect = numpy.random.choice(self.availableBlocks, p=p)
        return nodeIDtoConnect

    #Call node.connect on each node after the first one
    def Add_Connections(self):
        for node in self.nodeList:
            if node.ID != 0:
                nodeToConnect = self.nodeList[self.connect_TO()]
                #print("\nNode to Connect: ", nodeToConnect)
                node.connect(nodeToConnect)
                self.availableBlocks.append(node.ID)
                if nodeToConnect.full:
                    self.availableBlocks.remove(nodeToConnect.ID)
                if len(self.availableBlocks) == 5: 
                    self.availableBlocks.pop(0)

    def blockMiddle(self, node):
        blockMiddle = [0, 0, 0]
        prevDirection = node.previousNode.direction
        if prevDirection == 0: #add prevNode's xsize/2
            blockMiddle[0] = node.previousNode.xsize/2
        elif prevDirection == 1: #add prevNode's ysize/2
            blockMiddle[1] = node.previousNode.ysize/2
        elif prevDirection == 2: #add prevNode's zsize/2
            blockMiddle[2] = node.previousNode.zsize/2
        elif prevDirection == 3: #add prevNode's -xsize/2
            blockMiddle[0] = -node.previousNode.xsize/2
        elif prevDirection == 4: #add prevNode's -ysize/2
            blockMiddle[1] = -node.previousNode.ysize/2
        elif prevDirection == 5: #add prevNode's -zsize/2
            blockMiddle[2] = -node.previousNode.zsize/2
        
        return blockMiddle
    def Create_Body(self):
        
        #Generate Robot
        zdiff = self.initialZ
        
        
        #print("The Sensors: ", self.sensorTrue, "\n")

        pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")
        #Create connecting blocks
        
        for node in self.nodeList:
            if node.ID == 0:
                blockpos = [0, 0, zdiff]
            else:
                if node.direction == 0:
                    blockpos = [node.xsize/2, 0, 0]
                    if node.previousNode.ID == 0:
                        node.jointPos = [node.previousNode.xsize/2, 0, zdiff]
                    else:
                        blockprevMiddle = self.blockMiddle(node)
                        blockprevMiddle[0] = blockprevMiddle[0] + node.previousNode.xsize/2
                        node.jointPos = blockprevMiddle
                elif node.direction == 1:
                    blockpos = [0, node.ysize/2, 0]
                    if node.previousNode.ID == 0:
                        node.jointPos = [0, node.previousNode.ysize/2, zdiff]
                    else:
                        blockprevMiddle = self.blockMiddle(node)
                        blockprevMiddle[1] = blockprevMiddle[1] + node.previousNode.ysize/2
                        node.jointPos = blockprevMiddle
                elif node.direction == 2:
                    blockpos = [0, 0, node.zsize/2]
                    if node.previousNode.ID == 0:
                        node.jointPos = [0, 0, zdiff + node.previousNode.zsize/2]
                    else:
                        blockprevMiddle = self.blockMiddle(node)
                        blockprevMiddle[2] = blockprevMiddle[2] + node.previousNode.zsize/2
                        node.jointPos = blockprevMiddle
                elif node.direction == 3:
                    blockpos = [-node.xsize/2, 0, 0]
                    if node.previousNode.ID == 0:
                        node.jointPos = [-node.previousNode.xsize/2, 0, zdiff]
                    else:
                        blockprevMiddle = self.blockMiddle(node)
                        blockprevMiddle[0] = blockprevMiddle[0] - node.previousNode.xsize/2
                        node.jointPos = blockprevMiddle
                elif node.direction == 4:
                    blockpos = [0, -node.ysize/2, 0]
                    if node.previousNode.ID == 0:
                        node.jointPos = [0, -node.previousNode.ysize/2, zdiff]
                    else:
                        blockprevMiddle = self.blockMiddle(node)
                        blockprevMiddle[1] = blockprevMiddle[1] - node.previousNode.ysize/2
                        node.jointPos = blockprevMiddle
                elif node.direction == 5:
                    blockpos = [0, 0, -node.zsize/2]
                    if node.previousNode.ID == 0:
                        node.jointPos = [0, 0, zdiff - node.previousNode.zsize/2]
                    else:
                        blockprevMiddle = self.blockMiddle(node)
                        blockprevMiddle[2] = blockprevMiddle[2] - node.previousNode.zsize/2
                        node.jointPos = blockprevMiddle
                
                pyrosim.Send_Joint(name = str(node.previousNode.ID) + "_" + str(node.ID),
                                    parent= str(node.previousNode.ID), child= str(node.ID),
                                    type= "revolute", position= node.jointPos, jointAxis= node.jointDir)
            pyrosim.Send_Cube(name= str(node.ID), pos=blockpos , size=[node.xsize, node.ysize , node.zsize], color = self.Determine_Color(node))

            #lastSize = [xsize, ysize, zsize]
                
            """
            #Create joints if we are not in the last block (all revolute and X axis)
            if node.ID < self.blockNum-1:
                thisAxisidx = random.randint(0,2)
                if node.ID==0:
                    jointPos = [0, -ysize/2, zdiff]
                else:
                    jointPos = [0, -ysize, 0]
                pyrosim.Send_Joint(name = str(i) + "_" + str(i+1), parent= str(i), child= str(i+1),
                                       type="revolute", position= jointPos, jointAxis= jointDir[thisAxisidx])
            """      
        

          
    
        #pyrosim.Send_Joint(name = "Torso_FrontLeft" , parent= "Torso" , child = "FrontLeft" , type = "revolute", 
         #   position = [-0.25, -1+(width/2 - 0.1), legLength ], jointAxis = "0 1 0")
        
        pyrosim.End()

    def Create_Brain(self):  
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        
        sensorCount = 0
        motorCount = self.numSensorNeurons
        for node in self.nodeList:
            if node.isSensor:
                pyrosim.Send_Sensor_Neuron(name = sensorCount, linkName =str(node.ID))
                sensorCount +=1
            if node.ID != 0:
                pyrosim.Send_Motor_Neuron(name = motorCount, jointName= str(node.previousNode.ID)+"_"+ str(node.ID))
                motorCount += 1

        
        
        for currentRow in range(self.numSensorNeurons):
            for currentColumn in range(self.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName= currentRow, targetNeuronName= currentColumn+self.numSensorNeurons, 
                    weight= self.weights[currentRow][currentColumn])
        
        #pyrosim.Send_Sensor_Neuron(name = 5, linkName= "RightLower")
        

        #pyrosim.Send_Motor_Neuron(name = 16, jointName= "Torso_Right")
        #pyrosim.Send_Motor_Neuron(name = 17, jointName= "Right_RightLower")
        
        
        
        pyrosim.End()
        