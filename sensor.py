import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c


class SENSOR:

    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(c.loopRange)

    def GET_VALUE(self, timestep):
        self.values[timestep] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

        if timestep == c.loopRange - 1:
            print(self.linkName, self.values)

    def Save_Values(self):
        np.save(f"data/{self.linkName}SensorValues.npy", self.values)
