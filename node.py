import numpy as np
import random
import constants as c

class NODE:
    def __init__(self, ID):
        self.numConnections = 0
        self.full = False
        self.ID = ID
        #These connections are an array that corresponds to directions [x, y, z, -x, -y, -z]
        self.connections = np.zeros(6)
        #Create the block properties:
        self.xsize = random.uniform(c.mindim, c.maxdim)
        self.ysize = random.uniform(c.mindim, c.maxdim)
        self.zsize = random.uniform(c.mindim, c.maxdim)
        self.jointPos = [0, 0, 0]
        self.isSensor = random.randint(0,1) #50% chance block is a sensor
        


    def findDirection(self, otherNode):
        indexWanted = random.randint(0, 5-otherNode.numConnections)
        currentidx = 0
        for i in range(6):
            if otherNode.connections[i] == 0:
                if currentidx == indexWanted:
                    return i
                else:
                    currentidx += 1

    def connect(self, otherNode):
        self.direction = self.findDirection(self, otherNode) #Find side to add on to
        otherNode.connections[self.direction] = 1 #update previous node connection directions
        thisNodeDirection = (self.direction + 3) % 6
        self.connections[thisNodeDirection] = 1 #update this node's connection direction in opposite dir
        self.previousNode = otherNode
        otherNode.numConnections += 1 #Check if the otherNode is a full block
        if otherNode.numConnections == 6:
            otherNode.full = True
        

