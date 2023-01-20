import pyrosim.pyrosim as pyrosim
import random
def Generate_Body():
    #Generate World
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[-2, 2, 0.5] , size=[1, 1, 1])  
    pyrosim.End()
    #Generate Robot
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5] , size=[1, 1, 1])  
    pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1, 0, 1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5] , size=[1, 1, 1])  
    pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2, 0, 1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5] , size=[1, 1, 1])  
    
    pyrosim.End()

def Generate_Brain():
   #Generate Brain
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name = 0, linkName= "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1, linkName= "BackLeg")
    pyrosim.Send_Sensor_Neuron(name = 2, linkName= "FrontLeg")
    pyrosim.Send_Motor_Neuron(name = 3, jointName= "Torso_BackLeg")
    pyrosim.Send_Motor_Neuron(name = 4, jointName= "Torso_FrontLeg")
    for sensor in range(3):
        for motor in range(3, 5):
            pyrosim.Send_Synapse( sourceNeuronName= sensor, targetNeuronName= motor, weight= (random.random() * 2) - 1)
    pyrosim.End()


Generate_Body()
Generate_Brain()