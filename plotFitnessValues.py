import numpy as np
import math
import matplotlib.pyplot as mp
import matplotlib.colors as mcolors
import constants as c

# Alpha test
alphaFitnessValues = np.load("data/Alpha_Data_NP.npy")
alphaMeanValues = np.mean(alphaFitnessValues, axis=0)
alphaStdDevValues = np.std(alphaFitnessValues, axis=1)

# Beta test
betaFitnessValues = np.load("data/Beta_Data_NP.npy")
betaMeanValues = np.mean(betaFitnessValues, axis=0)
betaStdDevValues = np.std(betaFitnessValues, axis=1)

# Curve for each fitness
# for i in range(c.numberOfGenerations):
#     mp.plot(alphaFitnessValues[i, :], label=f"Alpha_Test_Row_{i}", linewidth=.5, color='r')
#     mp.plot(betaFitnessValues[i, :], label=f"Beta_Test_Row_{i}", linewidth =.5, color = 'b')

# Average fitness
# mp.plot(alphaMeanValues, label="Alpha_Mean_Values", color='m')
# mp.plot(betaMeanValues, label="Beta_Mean_Values", color='c')
# mp.legend()

# Standard Deviation
mp.plot(alphaMeanValues+alphaStdDevValues, label="Alpha_STD(+)", color='r')
mp.plot(alphaMeanValues, label="Alpha_Mean_Values", color='m')
mp.plot(alphaMeanValues-alphaStdDevValues, label="Alpha_STD(-)", color='y')
mp.plot(betaMeanValues+betaStdDevValues, label="Beta_STD(+)", color='g')
mp.plot(betaMeanValues, label="Beta_Mean_Values", color='b')
mp.plot(betaMeanValues-betaStdDevValues, label="Beta_STD(-)", color='c')
mp.legend()
mp.show()