import numpy

numberOfGenerations = 1
populationSize = 1
numSensorNeurons = 13
numMotorNeurons = 12
motorJointRange = 0.6
totalStep = 1000
verticalWeight = 10
airTimeWeight = 1
maxForce = 50
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