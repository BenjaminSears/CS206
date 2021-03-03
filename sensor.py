import pyrosim.pyrosim as pyrosim
import numpy as np

class SENSOR:

    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(100)

    def GET_VALUE(self, timestep):
        self.values[timestep] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
