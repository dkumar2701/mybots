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
        self.backConnections = {}
        #Create the block properties:
        self.xsize = random.uniform(c.mindim, c.maxdim)
        self.ysize = random.uniform(c.mindim, c.maxdim)
        self.zsize = random.uniform(c.mindim, c.maxdim)
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
        direction = self.findDirection(self, otherNode) #Find side to add on to
        otherNode.connections[direction] = 1 #update previous node connection directions
        self.backConnections[otherNode] = direction #update dictionary of back connections (used to connect blocks)
        otherNode.numConnections += 1 #Check if the otherNode is a full block
        if otherNode.numConnections == 6:
            otherNode.full = True
        
