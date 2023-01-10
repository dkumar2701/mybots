import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5
sumheight = 0
for i in range(10):
    pyrosim.Send_Cube(name="Box", pos=[x, y, z+(sumheight)] , size=[length, width, height])
    sumheight += (height/2 + (height*0.9)/2) 
    length = width = height = 0.9*length
    
pyrosim.End()