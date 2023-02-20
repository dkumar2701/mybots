# Assignment 7

TO RUN THE CODE:
Run the _runRandomBody.py_ file. This creates a new solution class of ID 0 (a random robot) and plays a simulation for this robot. This assignment does not include evolution, so each time this file is run, a new random robot is created

My code is primarily in the solution.py and node.py files, and correspond to the SOLUTION class (which creates a random robot) and the NODE class (which creates a random link, this readme will use NODE and link interchangeably). Code for the rest of the files was completed following the ludobots tutorials at www.reddit.com/r/ludobots. 

Below is a diagram showing conceptually how these brains and bodies are connected:


Each NODE object has the following attributes:
- numConnections = the number of other links attached to this NODE object.
- full = boolean identifying if this node is "full" of links and thus no other links may be attached. A node is "full" if numConnections == 4
- ID = an ID for this node object
- chainedto0 = boolean identifying if this node is part of the chain from the first node in the -y direction.
- lastChain = boolean identifying if this node is the last of its chain. This and chainedto0 are used to weight the robot creation into having a more elongated shape.
- connections = 6-element array of 1's and 0's corresponding to directions [x, y, z, -x, -y, -z]. Used to identify which sides have links connected
- xsize, ysize, and zsize = randomly generated values to determine NODE dimensions.
- jointPos = 3-element array identifying the position of the joint that this node connects to a previous link with 
- isSensor = randomly chosen boolean to determine if this node is a sensor (2/3 chance)
- previousNode = the NODE object that this node is connecting to
- direction = the face of the previous node that this node should be attached to

NODE objects have a function findDirection(self, otherNode) that assists in choosing an open direction on the otherNode to attach to.
NODE objects have a function connect(self, otherNode) that sets values such as the previousNode, and direction.





