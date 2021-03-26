import numpy as np
import math
import matplotlib.pyplot as mp

backLegSensorValues = np.load("data/backLegSensorValues.npy")
frontLegSensorValues = np.load("data/frontLegSensorValues.npy")
#mp.plot(backLegSensorValues, label="Back", linewidth=3)
#mp.plot(frontLegSensorValues, label="Front")
targetAngles = np.load("data/targetAngles.npy")
mp.plot(np.sin(targetAngles))
mp.legend()
mp.show()



