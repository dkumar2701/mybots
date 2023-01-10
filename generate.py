import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5
sumheight = 0
for row in range(5):
    for col in range(5):
        length = width = height = 1
        sumheight = 0
        for i in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x+(row), y+(col), z+(sumheight)] , size=[length, width, height])
            sumheight += 1 
            length = width = height = 0.9*length

    
pyrosim.End()