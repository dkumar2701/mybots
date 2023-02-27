from world import WORLD
from robot import ROBOT
import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
import pybullet_data
import time
class SIMULATION:
    def __init__(self, directOrGui, solutionID):
        self.directOrGui = directOrGui
        if directOrGui == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else: 
            self.physicsClient = p.connect(p.GUI)
            p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT(solutionID)
        pyrosim.Prepare_To_Simulate(self.robot.robotID)
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()
        #print("RAN INIT" + str(solutionID))

    def Run(self):
        #print("Running RUN"+ str(self.robot.robotID))
        for i in range(c.totalStep):
            #print(i)
            
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            
            if self.directOrGui == "GUI":
                time.sleep(1/c.totalStep)
            #print("Step Status: ", i)

    def Get_Fitness(self, solutionID):
        self.robot.Get_Fitness(solutionID)
            
    def __del__(self):
        for linkname, sensor in self.robot.sensors.items():
            sensor.Save_Values()
        p.disconnect()
        