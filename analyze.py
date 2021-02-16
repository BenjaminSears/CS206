import numpy as np
import matplotlib.pyplot as mp

backLegSensorValues = np.load("data/backLegSensorValues.npy")
mp.plot(backLegSensorValues)
mp.show()


