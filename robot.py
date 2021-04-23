import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import pybullet as p
import numpy as np
from sensor import SENSOR
from motor import MOTOR
import constants as c
import os

class ROBOT:

    def __init__(self, solutionID):
        self.motors = {}
        self.sensors = {}
        self.solutionID = solutionID
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate("body.urdf")
        self.nn = NEURAL_NETWORK("brain"+solutionID+".nndf")
        os.remove("brain" + self.solutionID+ ".nndf")
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

    def Think(self):
        self.nn.Update()
        self.nn.Print()

    def Act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].SET_VALUE(self.robot, desiredAngle * c.motorJointRange)

    def Get_Fitness(self):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]
        f = open("tmp"+str(self.solutionID)+".txt", "w")
        f.write(str(xPosition))
        f.close()
        os.rename("tmp"+str(self.solutionID)+".txt", "fitness"+str(self.solutionID)+".txt")
