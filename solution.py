import random
import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import time
import constants as c

length = 1
width = 1
height = 1

class SOLUTION:
    
    def __init__(self, inputID):
        self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons)
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
        x = -2
        y = -3
        z = .5
        for i in range(3):
            pyrosim.Send_Cube(name=f'Box_{i}', pos=[x, y, z], size=[length, width, height])
            y += 4
        x = -4
        y = -4
        for i in range(3):
            pyrosim.Send_Cube(name=f'Box_{i}', pos=[x, y, z], size=[length, width, height])
            y += 4
        x = -6
        y = -3
        for i in range(3):
            pyrosim.Send_Cube(name=f'Box_{i}', pos=[x, y, z], size=[length, width, height])
            y += 4
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        length = 1
        width = 1
        height = 1
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[length, width, height])

        pyrosim.Send_Joint(name="Torso_Front_Leg", parent="Torso", child="Front_Leg", type="revolute",
                           position="0, 0.5, 1.0", jointAxis="1 0 0")
        pyrosim.Send_Cube(name="Front_Leg", pos=[0.0, 0.5, 0], size=[0.2, 1.0, 0.2])

        pyrosim.Send_Joint(name="Torso_Back_Leg", parent="Torso", child="Back_Leg", type="revolute",
                           position="0.0, -0.5, 1.0", jointAxis="1 0 0")
        pyrosim.Send_Cube(name="Back_Leg", pos=[0.0, -0.5, 0], size=[0.2, 1.0, 0.2])

        pyrosim.Send_Joint(name="Torso_Left_Leg", parent="Torso", child="Left_Leg", type="revolute",
                           position="-0.5, 0.0, 1.0", jointAxis="0 1 0")
        pyrosim.Send_Cube(name="Left_Leg", pos=[-0.5, 0.0, 0], size=[1.0, 0.2, 0.2])

        pyrosim.Send_Joint(name="Torso_Right_Leg", parent="Torso", child="Right_Leg", type="revolute",
                           position="0.5, 0.0, 1.0", jointAxis="0 1 0")
        pyrosim.Send_Cube(name="Right_Leg", pos=[0.5, 0.0, 0], size=[1.0, 0.2, 0.2])

        pyrosim.Send_Joint(name="Front_Leg_Lower_Leg", parent="Front_Leg", child="Front_Lower_Leg", type="revolute",
                           position="0.0, 1.0, 0.0", jointAxis="1 0 0")
        pyrosim.Send_Cube(name="Front_Lower_Leg", pos=[0.0, 0.0, -0.5], size=[0.2, 0.2, 1.0])

        pyrosim.Send_Joint(name="Back_Leg_Lower_Leg", parent="Back_Leg", child="Back_Lower_Leg",
                           type="revolute", position="0.0, -1.0, 0.0", jointAxis="1 0 0")
        pyrosim.Send_Cube(name="Back_Lower_Leg", pos=[0.0, 0.0, -0.5], size=[0.2, 0.2, 1.0])

        pyrosim.Send_Joint(name="Left_Leg_Lower_Leg", parent="Left_Leg", child="Left_Lower_Leg", type="revolute",
                           position="-1.0, 0 0.0, 0.0", jointAxis="0 1 0")
        pyrosim.Send_Cube(name="Left_Lower_Leg", pos=[0.0, 0.0, -0.5], size=[0.2, 0.2, 1.0])

        pyrosim.Send_Joint(name="Right_Leg_Lower_Leg", parent="Right_Leg", child="Right_Lower_Leg",
                           type="revolute",
                           position="1.0, 0.0, 0.0", jointAxis="0 1 0")
        pyrosim.Send_Cube(name="Right_Lower_Leg", pos=[0.0, 0.0, -0.5], size=[0.2, 0.2, 1.0])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+ str(self.myID) +".nndf")

        pyrosim.Send_Motor_Neuron(name=0, jointName="Torso_Back_Leg")
        pyrosim.Send_Motor_Neuron(name=1, jointName="Torso_Front_Leg")
        pyrosim.Send_Motor_Neuron(name=2, jointName="Torso_Left_Leg")
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_Right_Leg")

        pyrosim.Send_Sensor_Neuron(name=4, linkName="Front_Lower_Leg")
        pyrosim.Send_Motor_Neuron(name=5, jointName="Front_Leg_Lower_Leg")

        pyrosim.Send_Sensor_Neuron(name=6, linkName="Back_Lower_Leg")
        pyrosim.Send_Motor_Neuron(name=7, jointName="Back_Leg_Lower_Leg")

        pyrosim.Send_Sensor_Neuron(name=8, linkName="Left_Lower_Leg")
        pyrosim.Send_Motor_Neuron(name=9, jointName="Left_Leg_Lower_Leg")

        pyrosim.Send_Sensor_Neuron(name=10, linkName="Right_Lower_Leg")
        pyrosim.Send_Motor_Neuron(name=11, jointName="Right_Leg_Lower_Leg")

        for currentRow in range(0,c.numSensorNeurons,1):
            for currentColumn in range(0,c.numMotorNeurons,1):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+c.numSensorNeurons,
                                     weight=self.weights[currentRow][currentColumn])
        pyrosim.End()

    def Mutate(self):
        randRow = random.randint(0, c.numSensorNeurons-1)
        randColumn = random.randint(0, c.numMotorNeurons-1)
        self.weights[randRow][randColumn] = random.random() * 2 - 1

    def Set_ID(self, inputID):
        self.myID = inputID
