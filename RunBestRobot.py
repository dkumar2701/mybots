import pickle

yn = input("Do you want to run a saved robot?(y/n)\n")
if yn == "n":
    print("Running the Best Robot from the last simulation")
    robotString = 'BestRobot.pickle'
elif yn == "y":
    id = input("Input the robot ID you want to see (should have a .pickle file associated with it)\n")
    robotString = 'Best'+id+'.pickle'
else:
    print("y/n answer only\n")
with open(robotString, 'rb') as f:
    data = pickle.load(f)


data.Start_Simulation("GUI")
print("\nBest Fitness = "+ str(data.fitness)+ "\n")