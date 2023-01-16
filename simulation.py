from world import WORLD
from robot import ROBOT
import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import time
class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT()
        pyrosim.Prepare_To_Simulate(self.robot.robotID)

    def Run(self):
        for i in range(1000):
            print(i)
            
            p.stepSimulation()
            #c.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            #c.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
            #pyrosim.Set_Motor_For_Joint(
            #bodyIndex = robotID,
            #jointName = "Torso_BackLeg",
            #controlMode = p.POSITION_CONTROL,
            #targetPosition = -c.targetAnglesBackLeg[i], 
            #maxForce = 75)
            #pyrosim.Set_Motor_For_Joint(
            #bodyIndex = robotID,
            #jointName = "Torso_FrontLeg",
            #controlMode = p.POSITION_CONTROL,
            #targetPosition = -c.targetAnglesFrontLeg[i], 
            #maxForce = 75)
            time.sleep(1/240)
            #print("Step Status: ", i)
    def __del__(self):
        p.disconnect()
        