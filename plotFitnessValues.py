import numpy as np
import math
import matplotlib.pyplot as mp
import constants as c

# Alpha test
alphaFitnessValues = np.load("data/Alpha_Data_NP.npy")

# Beta test
betaFitnessValues = np.load("data/Beta_Data_NP.npy")

# Curve for each fitness
for i in range(c.numberOfGenerations):
    mp.plot(alphaFitnessValues[i, :], label=f"Alpha_Test_Row_{i}", linewidth=.5, color='r')
    mp.plot(betaFitnessValues[i, :], label=f"Beta_Test_Row_{i}", linewidth =.5, color = 'b')

mp.legend()
mp.show()