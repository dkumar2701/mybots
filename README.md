# Final Project (use 16pt scale, Engineer)

## VIDEO SUMMARY:

## TO RUN THE CODE:
### Multiple Trials
Run the _RUNTRIALS.py_ file to run a number of parallel hill climber (**phc**) trials. This code calls _multSearch.py_ to run the trials, generates fitness curves for each trial (which is saved in _MultSearchFig.png_), shows a random robot from generation 0, and shows a simulation of the best robot across all trials. The popup fitness curves must be closed for the simulations to show. After the first simulation, press Enter to show the best robot simulation. 

**Playing with Sim:** Each simulation has the camera tracking the robot for ease of use. If you would like to interact with the simulation, comment out lines _36-37_ in _simulation.py_

You will be prompted to enter the **number of trials**, **robot population size**, and the **number of generations** to simulate. Each trial may take a seed, and this option is also prompted. If you choose not to input seeds, you may choose the lower and upper bounds of the randomly generated seeds. Seeds are later shown in the fitness graph and in SeedNumbers.txt. If you do opt to input seeds, you will be prompted to enter integer seeds to be used.

### Viewing Simulations
After running _RUNTRIALS.py_, the gen0 and best robot simulations you see are saved. These can be replayed by running _RunGen0.py_ or _RunBestRobot.py_ respectively. If you want to see the simulation of the last _RUNTRIALS_ again, enter "n" into the input. Otherwise, you may input "y" and then a number (1 or 2) to see simulations of robots I have evolved.

## Fitness Determination

Each child robot's fitness value is compared to its parent's value and the robot with the larger fitness "survives." The fitness function used is the robot's $YPosition_{final} - YPosition_{100thFrame}$. The start position is at the 100th frame to account for the robot falling at the start of the simulation, where its initial position may not be 0.

The direction of greatest fitness is the +Y direction, and is depicted by the black arrow below (x,y,z axis shown by red, green and blue arrows):
![image](https://user-images.githubusercontent.com/68355843/221733346-d9fa2968-86ae-41c3-9275-f1d821576e77.png)

## Example MultSearch with Seed List: [9, 5, 13, 11, 12]
### Fitness Curves
The following graph depicts 5 fitness curves from a multSearch with searchNum = 5. For each trial, the population size was 10 and the number of generations was 30.
The fitness curves represents the best fitness from each generation of robots.
<img src="https://user-images.githubusercontent.com/68355843/221740908-5389b6a3-39b4-4720-a067-baab802485c4.png" width="100%" />

### Random Robot and Best Robot
Below are gifs of a _random robot_ from **Gen 0** with **Fitness = 0.02801** and the _best robot_ from the 5 trials with **Fitness = 9.42344**

<img src="https://user-images.githubusercontent.com/68355843/221749743-9e44e971-c242-441c-b057-83eb27fc8fe9.gif" width="45%" /><img src="https://user-images.githubusercontent.com/68355843/221749946-ce11bccc-18d5-4663-8609-45524225ed52.gif" width="45%" />

## METHODS:

### Parallel Hill Climber Evolution: 

The evolution method used was parallel hill climber (phc). In phc, there is a permanent number of robots allowed in a population. In each generation, each of these robots has a "child", which is a copy of the parent with some mutation determined by the mutation function used. Fitness of parent and child are compared, and the robot with the greater fitness survives to create a child in the next generation. Below is a diagram of the phc process:

<img src="https://user-images.githubusercontent.com/68355843/225105798-889bd3bb-7431-4a48-9fb1-f94f65e88eb3.png" width="50%" />


### Robot Generation:

My code is primarily in the solution.py and node.py files, and correspond to the SOLUTION class (which creates a random robot) and the NODE class (which creates a random link, this readme will use NODE and link interchangeably). Robots are first created in the initialization of the SOLUTION class, with a random number of nodes and connections between nodes. Code for the rest of the files was completed following the ludobots tutorials at www.reddit.com/r/ludobots and pyrosim was used for robot simulations. Inspiration for robotic evolution from Karl Sims's work.

Below is an example of a randomly generated robot with 5 links. Green links have sensor neurons and blue links do not. Links are connected to one another by revolute joints which contain motor neurons. Every link is connected to a joint: 
<img src="https://user-images.githubusercontent.com/68355843/221752391-98ec4b5f-8f71-4f75-9f7f-4669f82e9b87.gif" width="50%">

Below is a diagram showing conceptually how these brains and bodies are connected with an example of a 4-link robot:
<img src="https://user-images.githubusercontent.com/68355843/221765839-88beb42f-1afc-4276-825a-4ec8c60ec073.jpg" width="50%" />

All joints have motor neurons and every sensor neuron is synapsed to all motor neurons.

### How Robots are Evolved

Robots are evolved as in ludobots, where one of the synapse weights in the child is changed randomly. Additionally, motors may evolve by adding or removing links. Adding or removing each has a 50% chance of occurring and only one may happen at a time during the mutation step, which is in the function _Mutate_ in the _SOLUTION_ class. Below are diagrams depicting the addition/removal of link 4:

<img src="https://user-images.githubusercontent.com/68355843/221766469-f5ae6f1d-c7bd-4f31-9d13-f6d0156314ef.jpg" width="49%" /><img src="https://user-images.githubusercontent.com/68355843/221766501-82f006b8-7f7e-4486-b318-82513687d3d4.jpg" width="49%" />

Here is a link to a youtube video showing more robot evolution examples: https://youtu.be/_U0uLyCg3BA

### Extra information on the NODE class:

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

## RESULTS

By using the fitness function described above, I was able to evolve robots to move very well in the y-direction. Below is a simulation which used **10 trials**, **population 10**, and **500 generations**. The first video is of a robot in generation 0, without any evolution which had a fitness of **bruh**. The second video depicts the best robot, which had a fitness of **bruh**. The fitness curves are also shown below. You may replay this robot using the number 1 as an input for _RunGen0.py_ and _RunBestRobot.py_.

<img src="https://user-images.githubusercontent.com/68355843/225154258-671beb95-eeb3-46b0-8fd6-5add6f3497aa.gif" width="45%" /><img src="https://user-images.githubusercontent.com/68355843/225154371-2dded6d3-299e-4f57-bd50-cecceeee36e9.gif" width="45%" />
![Figure2](https://user-images.githubusercontent.com/68355843/225154515-ad9a5c6c-a440-4c23-ba2f-3589bdd29e5c.png)

These results show that evolution was successful, and the robots added and removed limbs throughout the generations to create a final robot that had a noticeable hopping motion. Some earlier errors in evolution occurred due to the fitness function, which is based on the y-position of the robot's first link. Because of this, evolution sometimes lead to tall robots being created, allowing it to tip over and have a large y-value for the first link without locomotion. To prevent this, I changted the fitness function to the difference in y-positions, with the start position beginning 100 steps into the simulation to allow for the robot to fall first. After this, evolution worked smoothly.
Some other errors in evolution were due to bugs such as deleting limbs without deleting the corresponding brain neurons and synapses, which resulted in keyerrors when the robot was being simulated. However, these were fixed to have evolution work smoothly. 

An interesting point to note in these simulations is the presence of cyclic movement in the robots. No pattern generators were encoded into the robots. Rather, they evolved to use periodic motion in order to achieve a high level of locomotion.
