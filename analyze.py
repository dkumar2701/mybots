import numpy
import matplotlib.pyplot
backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')
targetAngles = numpy.load('data/targetAngles.npy')
print(backLegSensorValues)
#matplotlib.pyplot.plot(backLegSensorValues, label = "backLeg")
#matplotlib.pyplot.plot(frontLegSensorValues, label = "frontLeg")
matplotlib.pyplot.plot(targetAngles, label = "targetAngles")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()