import pybullet as p
import time
physicsClient = p.connect(p.GUI)
for i in range(1000):
    p.stepSimulation()
    time.sleep(0.5)
    print(i)
p.disconnect()