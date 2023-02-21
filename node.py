import numpy as np
import random
import constants as c

class NODE:
    def __init__(self, ID):
        self.numConnections = 0
        self.full = False
        self.ID = ID
        self.chainedto0 = False
        self.lastChain = False
        if self.ID == 0:
            self.chainedto0 = True
            self.lastChain = True
        
        #These connections are an array that corresponds to directions [x, y, z, -x, -y, -z]
        self.connections = np.zeros(6)
        #Create the block properties:
        if random.randint(0,1) == 1:
            subtractval = 0
        else: 
            subtractval = self.ID/10
        self.xsize = random.uniform(c.mindim, c.maxdim - subtractval)
        self.ysize = random.uniform(c.mindim, c.maxdim - subtractval)
        self.zsize = random.uniform(c.mindim, c.maxdim - subtractval)
        self.jointPos = [0, 0, 0]
        sensorChoices = [0, 1]
        sensorweights = [1,2]
        self.isSensor = random.choices(sensorChoices, weights=sensorweights, k=1)[0] #2/3 chance block is a sensor
        


    def findDirection(self, otherNode):
        directionList = []
        for i in range(6):
            if otherNode.connections[i] == 0:
                directionList.append(i)
        
        if otherNode.connections[4] == 0 and otherNode.chainedto0:
            newlist = [4]
            directionList.remove(4)
            weightlist = []
            newlist = newlist + directionList
            #Prefer to attach in the -y direction
            for i in range(len(newlist)):
                if i == 0:
                    weightlist.append(c.preferattachY)
                else:
                    weightlist.append(1)
            return random.choices(newlist, weights= weightlist, k=1)[0]
        else:
            weightlist = [1] * len(directionList)
            return random.choices(directionList, weights= weightlist, k=1)[0]
            



    def connect(self, otherNode):
        self.direction = self.findDirection(otherNode) #Find side to add on to
        if self.direction == 4 and otherNode.chainedto0:
            self.chainedto0 = True
            self.lastChain = True
            otherNode.lastChain = False
        #print("\nThis direction: ", self.direction)
        otherNode.connections[self.direction] = 1 #update previous node connection directions
        #print("\nNode ID: ", self.ID)
        #print("\nDirection: ", self.direction + 6)
        thisNodeDirection = (self.direction + 3) % 6
        self.connections[thisNodeDirection] = 1 #update this node's connection direction in opposite dir
        self.numConnections += 1
        self.previousNode = otherNode
        otherNode.numConnections += 1 #Check if the otherNode is a full block
        if otherNode.numConnections == 3:
            otherNode.full = True
        

