import numpy

numberOfGenerations = 10
populationSize = 10
numSensorNeurons = 6
numMotorNeurons = 12
motorJointRange = 1.0
totalStep = 1000
verticalWeight = 2
airTimeWeight = 10
yWeight = 20
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