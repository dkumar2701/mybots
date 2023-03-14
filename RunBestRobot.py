import pickle

with open('BestRobot.pickle', 'rb') as f:
    data = pickle.load(f)

data.Start_Simulation("GUI")