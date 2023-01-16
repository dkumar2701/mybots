import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import time
import numpy
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotID = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotID)
backLegSensorValues = numpy.zeros(1000)


for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    time.sleep(0.01)
    #print("Step Status: ", i)
p.disconnect()
print(backLegSensorValues)
numpy.save('data/test.npy', backLegSensorValues)