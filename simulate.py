import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import time
import numpy
import constants as c
import random
from simulation import SIMULATION
"""
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)



pyrosim.Prepare_To_Simulate(robotID)

#numpy.save('data/targetAnglesBack.npy', targetAnglesBackLeg)
#numpy.save('data/targetAnglesFront', targetAnglesFrontLeg)
#exit()
for i in range(1000):
    p.stepSimulation()
    c.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    c.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotID,
    jointName = "Torso_BackLeg",
    controlMode = p.POSITION_CONTROL,
    targetPosition = -c.targetAnglesBackLeg[i], 
    maxForce = 75)
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotID,
    jointName = "Torso_FrontLeg",
    controlMode = p.POSITION_CONTROL,
    targetPosition = -c.targetAnglesFrontLeg[i], 
    maxForce = 75)
    time.sleep(1/240)
    #print("Step Status: ", i)
p.disconnect()
print(c.backLegSensorValues)
numpy.save('data/backLegSensorValues.npy', c.backLegSensorValues)
numpy.save('data/frontLegSensorValues.npy', c.frontLegSensorValues)
"""
simulation = SIMULATION()