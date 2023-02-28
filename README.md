# Assignment 7

## TO RUN THE CODE:
### Multiple Trials
Run the _multSearch.py_ file to run **searchNum** number of parallel hill climber (**phc**) trials. This code runs the trials, generates fitness curves for each trial (which is saved in _MultSearchFig.png_), shows a random robot from generation 0, and shows a simulation of the best robot across all trials. The popup fitness curves must be closed for the simulations to show.

If you want to run only one trial, set searchNum = 1

### Change Generation and Population
To change the number of generations or the population size of each generation, you can alter the **c.numberOfGenerations** and **populationSize** variables in _constants.py_

### Seeding the Multiple Search
_multSearch.py_ has the functionality for you to be able to set random seeds. Each phc trial must have a different seed.

NO SEEDING: Set **usingSeeds** to False. After _multSearch.py_ runs, the seeds used for that run will be printed in a list of size **searchNum**

With SEEDING: Set **usingSeeds** to True. Set **seedList** to your list of seeds next to the comment on line 13

## Fitness Determination

Each child robot's fitness value is compared to its parent's value and the robot with the larger fitness "survives." The fitness function used is the robot's $YPosition_(final) - YPosition_(100thFrame)$. The start position is at the 100th frame to account for the robot falling at the start of the simulation, where its initial position may not be 0.

The direction of greatest fitness is the +Y direction, and is depicted by the black arrow below (x,y,z axis shown by red, green and blue arrows):
![image](https://user-images.githubusercontent.com/68355843/221733346-d9fa2968-86ae-41c3-9275-f1d821576e77.png)

## Example MultSearch with Seed List: [9, 5, 13, 11, 12]
### Fitness Curves
The following graph depicts 5 fitness curves from a multSearch with searchNum = 5. For each trial, the population size was 10 and the number of generations was 30.
The fitness curves represents the best fitness from each generation of robots.
<img src="https://user-images.githubusercontent.com/68355843/221740908-5389b6a3-39b4-4720-a067-baab802485c4.png" width="100%" />

### Random Robot and Best Robot
Below are gifs of a _random robot_ from **Gen 0** with **Fitness = d** and the _best robot_ from the 5 trials with **Fitness = d**



My code is primarily in the solution.py and node.py files, and correspond to the SOLUTION class (which creates a random robot) and the NODE class (which creates a random link, this readme will use NODE and link interchangeably). Code for the rest of the files was completed following the ludobots tutorials at www.reddit.com/r/ludobots and pyrosim was used for robot simulations. 

Below is a diagram showing conceptually how these brains and bodies are connected:
![Long image 02-20-2023 17 31](https://user-images.githubusercontent.com/68355843/220213085-07b2da2f-8ddd-428a-8910-ea943626556f.jpg)

All joints have motor neurons and every sensor neuron is synapsed to all motor neurons.

Each NODE object has the following attributes:
- numConnections = the number of other links attached to this NODE object.
- full = boolean identifying if this node is "full" of links and thus no other links may be attached. A node is "full" if numConnections == 3
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





