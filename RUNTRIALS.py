from multSearch import multSearch
import constants as c

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


print("\nLET'S START!!!\n")

multSearch(searchNum)

