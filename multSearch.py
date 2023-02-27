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
    if (i == 0):
        bestSOL = phc.bestLast_fitness
        bestFitness = phc.bestLast_fitness.fitness
    else:
        if (phc.bestLast_fitness.fitness > bestFitness):
            bestSOL = phc.bestLast_fitness
            bestFitness = bestSOL.fitness
    


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
plt.legend()
plt.savefig("MultSearchFig.png")
plt.show()
plt.close()

randomSolution = phc.bestFirst_fitness
print("RANDOM FITNESS: ", randomSolution.fitness, "\n")
randomSolution.Start_Simulation("GUI")
randomSolution.Wait_For_Simulation_To_End()
print("BEST OVERALL FITNESS: ", bestFitness, "\n")
bestSOL.Start_Simulation("GUI")
bestSOL.Wait_For_Simulation_To_End()
    
