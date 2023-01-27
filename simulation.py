from world import WORLD
from robot import ROBOT
import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import time
class SIMULATION:
    def __init__(self, directOrGui):
        self.directOrGui = directOrGui
        if directOrGui == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else: 
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT()
        pyrosim.Prepare_To_Simulate(self.robot.robotID)
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()

    def Run(self):
        for i in range(500):
            #print(i)
            
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            
            if self.directOrGui == "GUI":
                time.sleep(1/1000)
            #print("Step Status: ", i)

    def Get_Fitness(self):
        self.robot.Get_Fitness()
            
    def __del__(self):
        for linkname, sensor in self.robot.sensors.items():
            sensor.Save_Values()
        p.disconnect()
        