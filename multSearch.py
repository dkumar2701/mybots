import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import numpy as np
import constants as c
import matplotlib.pyplot as plt

searchNum = 5
bestAcrossSearches = np.zeros((0, c.numberOfGenerations + 1))
for i in range(5):
    phc = PARALLEL_HILL_CLIMBER()
    phc.Evolve()
    phc.Show_Best(False)
    bestArray = phc.bestEachGen
    bestAcrossSearches = np.vstack((bestAcrossSearches, bestArray))

f = open("MultSearchArray.txt", "w")
f.write(str(bestAcrossSearches))
f.close()

plt.title("Best Fitness of Each Generation")
plt.xlabel("Generation Number")
plt.ylabel("Fitness")
x = np.arange(c.numberOfGenerations + 1)
for i in range(5):
    y = bestAcrossSearches[i]
    plt.plot(x, y, label = "PHC #: "+ str(i))
plt.show()
plt.savefig("MultSearchFig.png")
    
