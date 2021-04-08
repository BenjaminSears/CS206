import random
import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import time

length = 1
width = 1
height = 1

class SOLUTION:
    
    def __init__(self, inputID):
        self.weights = np.random.rand(3,2)
        self.weights = self.weights * 2 - 1
        self.fitness = 0
        self.myID = inputID

    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("start /B python3 simulate.py " + directOrGUI + " " + str(self.myID))
        while not os.path.exists("fitness"+str(self.myID)+".txt"):
            time.sleep(0.01)
        f = open("fitness"+str(self.myID)+".txt", "r")
        self.fitness = float(f.readline())
        f.close()

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("start /B python3 simulate.py " + directOrGUI + " " + str(self.myID))

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness"+str(self.myID)+".txt"):
            time.sleep(0.01)
        f = open("fitness"+str(self.myID)+".txt", "r")
        self.fitness = float(f.readline())
        f.close()
        os.remove("fitness"+str(self.myID)+".txt")

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        # pyrosim.Send_Cube(name="Box", pos=[-3,3,.5], size=[length, width, height])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[length, width, height])

        pyrosim.Send_Joint(name="Torso_Front_Leg", parent="Torso", child="Front_Leg", type="revolute",
                           position="2.0, 0.0, 1.0")
        pyrosim.Send_Cube(name="Front_Leg", pos=[.5, 0, -.5], size=[length, width, height])

        pyrosim.Send_Joint(name="Torso_Back_Leg", parent="Torso", child="Back_Leg", type="revolute",
                           position="1.0, 0.0, 1.0")
        pyrosim.Send_Cube(name="Back_Leg", pos=[-.5, 0, -.5], size=[length, width, height])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+ str(self.myID) +".nndf")

        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="Back_Leg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="Front_Leg")

        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_Back_Leg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_Front_Leg")

        for currentRow in range(0,3,1):
            for currentColumn in range(0,2,1):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+3,
                                     weight=self.weights[currentRow][currentColumn])
        pyrosim.End()

    def Mutate(self):
        randRow = random.randint(0, 2)
        randColumn = random.randint(0, 1)
        self.weights[randRow][randColumn] = random.random() * 2 - 1

    def Set_ID(self, inputID):
        self.myID = inputID
