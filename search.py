from parallelHillClimber import *
import numpy as np

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()
np.savetxt("C:/Users/benja/Desktop/CS206/Projects/Hillclimber/data/A_Data.txt", c.data)
# for i in range(5):
#     os.system("python3 generate.py")
#     os.system("python3 simulate.py")