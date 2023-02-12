# Assignment 6

My code is built on the evolution code from previous assignments and thus running search.py will still print out a fitness based on the current fitness function, which can be ignored for this assignment. Running search.py will generate a random jointed, motorized, innervated, sensorized snake with a length between 2 and 6 blocks. Each block has random dimensions, each of which may be between 0.25 and 1. Additionally, each block has a 50% chance of being a sensor, in which case its color will be green rather than the standard blue. Each robot has at least 1 sensor. Each sensor neuron is connected to a motor neuron by a synapse. The axis of each joint is also randomly chosen between the x, y, and z direction. Snakes are created at a height tall enough for the maximum dimension of a block, thus preventing clipping into the ground.

TO RUN THE CODE:

To see random snakes, run search.py multiple times. 

The current settings are 0 generations with a population size of 1. Because this is still build on the evolution code, running search.py will create two simulations, each with a randomly generated snake. The current code makes the first and second snake only differ by block dimensions, so to create fully random snakes, run search.py again and ignore the second simulation that appears.
