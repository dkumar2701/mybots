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
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()

    def Run(self):
        for i in range(1000):
            #print(i)
            
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            
            time.sleep(1/60)
            #print("Step Status: ", i)
            
    def __del__(self):
        for linkname, sensor in self.robot.sensors.items():
            sensor.Save_Values()
        p.disconnect()
        