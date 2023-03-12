from multSearch import multSearch
import constants as c

print("Let's Evolve some Robots!\n")
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

