import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import numpy as np
import constants as c
import matplotlib.pyplot as plt
import random

searchNum = 5
bestAcrossSearches = np.zeros((0, c.numberOfGenerations + 1))
usingSeeds = False
if usingSeeds == False:
    seedList = []
else: 
    seedList = list(np.arange(searchNum)) #Change this to list of seeds you want
for i in range(searchNum):
    if usingSeeds == False:
        thisSeed = random.randint(0, searchNum *2)
        seedList.append(thisSeed)
        random.seed(thisSeed)
    else:
        random.seed(seedList[i])
    print("Trial #: ", i, "\n")
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

print("SEEDLIST: ", seedList, "\n")
    
