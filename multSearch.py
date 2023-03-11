import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import numpy as np
import constants as c
import matplotlib.pyplot as plt

os.system("del SeedNumber*.txt")
searchNum = 5
bestAcrossSearches = np.zeros((0, c.numberOfGenerations + 1))
usingSeeds = True # Set to true or false if using your own seeds
if usingSeeds == False:
    seedList = []
else: 
    seedList = [9, 5, 13, 11, 12] #Change this to list of seeds you want
for i in range(searchNum):
    if usingSeeds == False:
        thisSeed = np.random.randint(0, searchNum *3)
        seedList.append(thisSeed)
        
    else:
        thisSeed = seedList[i]
    file = open("SeedNumber"+str(thisSeed)+".txt", "w")
    file.write("The seed number is: "+str(thisSeed))
    file.close()
    np.random.seed(thisSeed)
    print("Trial #: ", i, "\n")
    phc = PARALLEL_HILL_CLIMBER()
    phc.Evolve()
    phc.Show_Best(False)
    bestArray = phc.bestEachGen
    bestAcrossSearches = np.vstack((bestAcrossSearches, bestArray))
    if (i == 0):
        bestSOL = phc.bestLast_fitness
        bestFitness = phc.bestLast_fitness.fitness
        bestPHC = phc
    else:
        if (phc.bestLast_fitness.fitness > bestFitness):
            bestSOL = phc.bestLast_fitness
            bestFitness = bestSOL.fitness
            bestPHC = phc
    


f = open("MultSearchArray.txt", "w")
f.write(str(bestAcrossSearches))
f.close()

plt.title("Best Fitness of Each Generation")
plt.xlabel("Generation Number")
plt.ylabel("Fitness")
x = np.arange(c.numberOfGenerations + 1)
for i in range(searchNum):
    y = bestAcrossSearches[i]
    plt.plot(x, y, label = "PHC #: "+ str(i))
plt.legend()
plt.savefig("MultSearchFig.png")
plt.show()
plt.close()

"""
randomSolution = phc.bestFirst_fitness
print("RANDOM FITNESS: ", randomSolution.fitness, "\n")
randomSolution.Start_Simulation("GUI")
randomSolution.Wait_For_Simulation_To_End()
print("\nBEST OVERALL FITNESS: ", bestFitness, "   ", bestSOL.fitness , "\n")
bestSOL.Start_Simulation("GUI")
#bestSOL.Wait_For_Simulation_To_End()
"""
bestPHC.Show_Best()

print("SEEDLIST: ", seedList, "\n")
    
