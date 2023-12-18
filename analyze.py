import numpy
import matplotlib.pyplot
backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')
targetAnglesBackLeg = numpy.load('data/targetAnglesBack.npy')
targetAnglesFrontLeg = numpy.load('data/targetAnglesFront.npy')
print(backLegSensorValues)
#matplotlib.pyplot.plot(backLegSensorValues, label = "backLeg")
#matplotlib.pyplot.plot(frontLegSensorValues, label = "frontLeg")
matplotlib.pyplot.plot(targetAnglesBackLeg, label = "targetAnglesBack")
matplotlib.pyplot.plot(targetAnglesFrontLeg, label = "targetAnglesFront")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()