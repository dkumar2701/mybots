import numpy

#For Random Body
maxdim = 1
mindim = 0.25

minlen = 4
maxlen = 7

zdiff = 2

#Constants for preferring last chain and preference of direction
preferLastChain = 3
preferattachY = 2

numberOfGenerations = 0
populationSize = 2
#numSensorNeurons = 5
#numMotorNeurons = 11
motorJointRange = 0.5
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