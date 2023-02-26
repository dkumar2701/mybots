from solution import SOLUTION
import constants as c
import copy
import os
import random
import numpy as np

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        os.system("del array*.txt")
        os.system("del body*.urdf")
        self.parents = {}
        self.nextAvailableID = 0
        self.fitnessArray = np.zeros((c.numberOfGenerations+1, c.populationSize))
        for i in range (c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
    
    def Evolve(self):
        
        self.Evaluate(self.parents, True)
        
        
        #self.parent.Evaluate("GUI")
        for currentGeneration in range (c.numberOfGenerations):
            self.Evolve_For_One_Generation(currentGeneration)
        

    def Evolve_For_One_Generation(self, currentGeneration):
        
        
        self.Spawn()
        
        self.Mutate()

        self.Evaluate(self.children, False)
        
        self.Print(currentGeneration)
        
        self.Select(currentGeneration)
        
            
    def Spawn(self):
        self.children = {}
        for i in self.parents.keys():
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID +=1

        
        
    def Mutate(self):
        for i in self.children.keys():
            self.children[i].Mutate()

    def Print(self, currentGeneration):
        print("\n")
        print("CURRENT GENERATION: ", currentGeneration)
        for i in self.parents.keys():  
            print("Parent Fitness_", i, ": ", self.parents[i].fitness, "  Child Fitness_", i, ": ", self.children[i].fitness)
            self.fitnessArray[currentGeneration, i] = self.parents[i].fitness
            
        print("\n")



    def Select(self, currentGeneration):
        for i in self.parents.keys():

            if self.parents[i].fitness < self.children[i].fitness:
                self.parents[i] = self.children[i]
            else:
                self.parents[i] = self.parents[i]
            if currentGeneration == c.numberOfGenerations -1:
                self.fitnessArray[currentGeneration+1, i] = self.parents[i].fitness
        
    def Evaluate(self, solutions, firstbool):
        if firstbool:
            """
            solutions[0].Start_Simulation("GUI")
            solutions[0].Wait_For_Simulation_To_End()
            self.firstfitness = self.parents[0].fitness
            """
            for i in range(c.populationSize):
                solutions[i].Start_Simulation("DIRECT")
            for i in range(c.populationSize):
                solutions[i].Wait_For_Simulation_To_End()
            randomid = random.randrange(c.populationSize)
            self.bestFirst_fitness = self.parents[randomid]
        else:
            for i in range(c.populationSize):
                solutions[i].Start_Simulation("DIRECT")
            for i in range(c.populationSize):
                solutions[i].Wait_For_Simulation_To_End()

    def Show_Best(self):
        best_fitness_idx = 0
        best_fitness = self.parents[0]
        for i in range(1, c.populationSize):
            if (self.parents[i].fitness > best_fitness.fitness):
                best_fitness = self.parents[i]
                best_fitness_idx = i
        self.bestLast_fitness = best_fitness
        self.TotalFitnesstxt()
        print("\nFIRST FITNESS: ", self.bestFirst_fitness.fitness, "\n")
        self.bestFirst_fitness.Start_Simulation("GUI")
        self.bestFirst_fitness.Wait_For_Simulation_To_End()
        print("\n BEST FITNESS: ", self.bestLast_fitness.fitness, "\n")
        self.bestLast_fitness.Start_Simulation("GUI")
        
    
    def TotalFitnesstxt(self):
        myFile = open('TotalFitnessArray.txt', 'w')
        myFile.write(str(self.fitnessArray))
        myFile.close()