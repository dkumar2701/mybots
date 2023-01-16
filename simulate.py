import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import time
import numpy
import constants as c
import random
from simulation import SIMULATION
"""


#numpy.save('data/targetAnglesBack.npy', targetAnglesBackLeg)
#numpy.save('data/targetAnglesFront', targetAnglesFrontLeg)
#exit()

p.disconnect()
print(c.backLegSensorValues)
numpy.save('data/backLegSensorValues.npy', c.backLegSensorValues)
numpy.save('data/frontLegSensorValues.npy', c.frontLegSensorValues)
"""
simulation = SIMULATION()
simulation.Run()