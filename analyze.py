import numpy
import matplotlib.pyplot
backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
print(backLegSensorValues)
matplotlib.pyplot.plot(backLegSensorValues)
matplotlib.pyplot.title("BackLeg")
matplotlib.pyplot.show()