from parallelHillClimber import *
import numpy as np

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()
np.savetxt("C:/Users/benja/Desktop/CS206/Projects/Hillclimber/data/Beta_Data.txt", c.data, fmt=('%10.3f'))
np.savetxt("C:/Users/benja/Desktop/CS206/Projects/Hillclimber/data/Beta_Data_NP", c.data, fmt=('%10.3f'))
# for i in range(5):
#     os.system("python3 generate.py")
#     os.system("python3 simulate.py")