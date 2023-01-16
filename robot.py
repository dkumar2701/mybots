import pybullet as p
class ROBOT:
    def __init__(self):
        self.sensors = {}
        self.motors = {}
        self.robotID = p.loadURDF("body.urdf")