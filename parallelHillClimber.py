from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        for i in range (c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
    
    def Evolve(self):
        
        self.Evaluate(self.parents)
        
        
        #self.parent.Evaluate("GUI")
        for currentGeneration in range (c.numberOfGenerations):
            self.Evolve_For_One_Generation()
        

    def Evolve_For_One_Generation(self):
        
        
        self.Spawn()
        
        self.Mutate()

        self.Evaluate(self.children)
        
        self.Print()
        
        self.Select()
        
            
    def Spawn(self):
        self.children = {}
        for i in self.parents.keys():
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID +=1

        
        
    def Mutate(self):
        for i in self.children.keys():
            self.children[i].Mutate()

    def Print(self):
        for i in self.parents.keys():  
            print("\n")
            print("Parent Fitness: ", self.parents[i].fitness, "  Child Fitness: ", self.children[i].fitness)
            print("\n")

    def Select(self):
        for i in self.parents.keys():

            if self.parents[i].fitness > self.children[i].fitness:
                self.parents[i] = self.children[i]
            else:
                self.parents[i] = self.parents[i]

    def Evaluate(self, solutions):
        for i in range(c.populationSize):
            solutions[i].Start_Simulation("DIRECT")
        for i in range(c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()

    def Show_Best(self):
        best_fitness_idx = 0
        best_fitness = self.parents[0]
        for i in range(1, c.populationSize):
            if (self.parents[i].fitness < best_fitness.fitness):
                best_fitness = self.parents[i]
                best_fitness_idx = i
        
        self.parents[best_fitness_idx].Start_Simulation("GUI")