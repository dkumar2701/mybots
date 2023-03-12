import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import numpy as np
import constants as c
import matplotlib.pyplot as plt
def multSearch(searchNum, usingSeeds, seedList):
        
    os.system("del SeedNumbers.txt")
    
    bestAcrossSearches = np.zeros((0, c.numberOfGenerations + 1))
    file = open("SeedNumbers.txt", "w")
    for i in range(searchNum):
        thisSeed = seedList[i]
        
        file.write("The "+ str(i)+"th trial's seed is: "+ str(thisSeed) + "\n")
        
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
    file.close()   


    f = open("MultSearchArray.txt", "w")
    f.write(str(bestAcrossSearches))
    f.close()

    plt.title("Best Fitness of Each Generation")
    plt.xlabel("Generation Number")
    plt.ylabel("Fitness")
    x = np.arange(c.numberOfGenerations + 1)
    for i in range(searchNum):
        y = bestAcrossSearches[i]
        plt.plot(x, y, label = "PHC seed #: "+ str(seedList[i]))
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
        
