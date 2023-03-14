import pickle

with open('Gen0.pickle', 'rb') as f:
    data = pickle.load(f)

data.Start_Simulation("GUI")