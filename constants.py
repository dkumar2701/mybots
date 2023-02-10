import numpy

#For Random Body
maxdim = 2
mindim = 0.5

minlen = 1
maxlen = 10


numberOfGenerations = 1
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