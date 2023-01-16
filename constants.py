import numpy

backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
x = numpy.linspace(0, 2* numpy.pi, 1000)
amplitudeBackLeg = numpy.pi/8
frequencyBackLeg = 10
phaseOffsetBackLeg= numpy.pi/2
targetAnglesBackLeg = numpy.sin(frequencyBackLeg*x + phaseOffsetBackLeg) * amplitudeBackLeg

amplitudeFrontLeg = numpy.pi/8
frequencyFrontLeg = 10
phaseOffsetFrontLeg= 0
targetAnglesFrontLeg = numpy.sin(frequencyFrontLeg*x + phaseOffsetFrontLeg) * amplitudeFrontLeg