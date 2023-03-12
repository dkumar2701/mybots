from multSearch import multSearch
import constants as c
import numpy as np

print("\nLet's Evolve some Robots!\n")
while(True):
    trialInput = input("Please input how many trials you would like to do: \n")
    
    if trialInput == "":
        print("You need to give me an integer")
    else:
        try: 
            val = int(trialInput)
        except ValueError:
            print("You need to give me an integer")
        else: 
            break

searchNum = int(trialInput)

while(True):
    popSizeinput = input("Please input how large the robot population should be: \n")
    
    if popSizeinput == "":
        print("You need to give me an integer")
    else:
        try: 
            val1 = int(popSizeinput)
        except ValueError:
            print("You need to give me an integer")
        else: 
            break

c.populationSize = int(popSizeinput)

while(True):
    genInput = input("Please input how many generations a trial should run for: \n")
    
    if genInput == "":
        print("You need to give me an integer")
    else:
        try: 
            val2 = int(genInput)
        except ValueError:
            print("You need to give me an integer")
        else: 
            break

c.numberOfGenerations = int(genInput)

while(True):
    seedinp = input("Do you have a list of seeds to input for the trials? (y/n)")
    if seedinp == "n":
        seedList = []
        usingSeeds = False
        for i in range(searchNum):
            rng = np.random.default_rng()
            seedList = list(rng.choice(searchNum*2, size=searchNum, replace=False))
        break
    elif seedinp == "y":
        seedList = []
        usingSeeds = True
        print("Write each integer seed and press ENTER")
        for i in range(searchNum):
            seedGiven = input("Type seed below: ")
            seedList.append(seedGiven)
        break
    else:
        print("Only type y or n")
            
print("\nLET'S START!!!\n")

multSearch(searchNum, usingSeeds, seedList)

