import numpy

#For Random Body
maxdim = 1
mindim = 0.25

minlen = 2
maxlen = 6

zdiff = 3

#Constants for preferring last chain and preference of direction
preferLastChain = 100
preferattachY = 1

numberOfGenerations = 0
populationSize = 1
numSensorNeurons = 5
numMotorNeurons = 11
motorJointRange = 1.0
totalStep = 2500
verticalWeight = 2
airTimeWeight = 10
yWeight = 2
maxForce = 75
"""
x = numpy.linspace(0, 2* numpy.pi, 1000)
amplitudeBackLeg = numpy.pi/4
frequencyBackLeg = 2
phaseOffsetBackLeg= 0
targetAnglesBackLeg = numpy.sin(frequencyBackLeg*x + phaseOffsetBackLeg) * amplitudeBackLeg

amplitudeFrontLeg = numpy.pi/8
frequencyFrontLeg = 10
phaseOffsetFrontLeg= 0
targetAnglesFrontLeg = numpy.sin(frequencyFrontLeg*x + phaseOffsetFrontLeg) * amplitudeFrontLeg
"""