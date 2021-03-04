import pyrosim.pyrosim as pyrosim
import pybullet as p
import numpy as np
from sensor import SENSOR
from motor import MOTOR

class ROBOT:

    def __init__(self):
        self.motors = {}
        self.sensors = {}
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate("body.urdf")
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Sense(self, timestep):
        for sensor in self.sensors.values():
            sensor.GET_VALUE(timestep)

    def Act(self, timestep):
        for motor in self.motors.values():
            motor.SET_VALUE(self.robot, timestep)

