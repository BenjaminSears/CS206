import pyrosim.pyrosim as pyrosim
import pybullet as p
import numpy as np
from sensor import SENSOR

class ROBOT:

    def __init__(self):
        self.motors = {}
        self.sensors = {}
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate("body.urdf")
        self.Prepare_To_Sense()

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, timestep):
        for sensor in self.sensors.values():
            sensor.GET_VALUE(timestep)

