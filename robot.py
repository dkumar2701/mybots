import pybullet as p
class ROBOT:
    def __init__(self):
        self.robotID = p.loadURDF("body.urdf")
        self.sensors = {}
        self.motors = {}
        
    def Prepare_To_Sense(self):
        pass