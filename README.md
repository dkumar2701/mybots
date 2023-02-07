# mybots

My code generates a robot that evolves to climb a small wall. After some trial and error (because we are not yet evolving bodies), I found that a long body for the robot with legs to its sides (like a crocodile) worked the best. The robot also has a tail, which I have noticed helps it jump over the wall.

TO RUN THE CODE:

Run search.py. The current settings are 30 generations with a population size of 15.

The fitness function I am using optimizes for largest fitness, where fitness = yPosition*c.yWeight - np.abs(xPosition).

the yPosition is used because I want the robot to move in the positive y direction, over the obstacle. c.yWeight is a constant used to increase the importance of the yPosition in the fitness function. I also subtract the absolute value of the xPosition to prevent the robot from accidentally going around the obstacle. 

Additionally, there is an optional part of the fitness function (that I do not use currently) that increases fitness based on the maximum height of the robot. This was calculated by keeping track of teh robot's z-position in every frame.
