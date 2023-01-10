import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("box.sdf")
length = 1
width = 2
height = 3
pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[length, width, height])
pyrosim.End()