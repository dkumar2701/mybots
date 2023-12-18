from solution import SOLUTION
import os

os.system("del brain*.nndf")
os.system("del fitness*.txt")
os.system("del array*.txt")
randomBody = SOLUTION(0)
randomBody.Start_Simulation("GUI")