import pybullet as p
class WORLD:
    def __init__(self):
        self.planeId = p.loadURDF("plane.urdf")
        self.robotID = p.loadURDF("body.urdf")