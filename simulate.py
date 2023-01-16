import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import time
import numpy
import random
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotID = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotID)
backLegSensorValues = numpy.zeros(10000)
frontLegSensorValues = numpy.zeros(10000)


for i in range(10000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotID,
    jointName = "Torso_BackLeg",
    controlMode = p.POSITION_CONTROL,
    targetPosition = (random.random() * numpy.pi) - numpy.pi/2, 
    maxForce = 75)
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotID,
    jointName = "Torso_FrontLeg",
    controlMode = p.POSITION_CONTROL,
    targetPosition = (random.random() * numpy.pi) - numpy.pi/2, 
    maxForce = 75)
    time.sleep(0.01)
    #print("Step Status: ", i)
p.disconnect()
print(backLegSensorValues)
numpy.save('data/backLegSensorValues.npy', backLegSensorValues)
numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)