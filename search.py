import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import numpy as np
"""
for i in range(5):
    os.system("python3 generate.py")
    os.system("python3 simulate.py")
"""
#thisSeed = np.random.randint(0, 20)
#np.random.seed(thisSeed)
phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
#print("The seed used was: ", thisSeed, "\n")
phc.Show_Best()
