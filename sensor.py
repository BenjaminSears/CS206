import pyrosim.pyrosim as pyrosim
import numpy as np

class SENSOR:

    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(100)
        print(self.values)


    def GET_VALUE(self):
        #backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Back_Leg")
        pass