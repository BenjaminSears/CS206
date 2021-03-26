import pyrosim.pyrosim as pyrosim
import random
length = 1
width = 1
height = 1


def Create_World():
    pyrosim.Start_SDF("world.sdf")
    # pyrosim.Send_Cube(name="Box", pos=[-3,3,.5], size=[length, width, height])
    pyrosim.End()


def Generate_Body():
    pyrosim.Start_URDF("body.urdf")

    pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[length, width, height])

    pyrosim.Send_Joint(name="Torso_Front_Leg", parent="Torso", child="Front_Leg", type="revolute",
                       position="2.0, 0.0, 1.0")
    pyrosim.Send_Cube(name="Front_Leg", pos=[.5, 0, -.5], size=[length, width, height])

    pyrosim.Send_Joint(name="Torso_Back_Leg", parent="Torso", child="Back_Leg", type="revolute",
                       position="1.0, 0.0, 1.0")
    pyrosim.Send_Cube(name="Back_Leg", pos=[-.5, 0, -.5], size=[length, width, height])

    pyrosim.End()


def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")

    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="Back_Leg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="Front_Leg")

    pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_Back_Leg")
    pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_Front_Leg")

    for sensorNeuron in range(0, 3, 1):
        for motorNeuron in range(3, 5, 1):
            weight = random.uniform(-1, 1)
            pyrosim.Send_Synapse(sourceNeuronName=sensorNeuron, targetNeuronName=motorNeuron, weight=weight)
    pyrosim.End()


Create_World()
Generate_Body()
Generate_Brain()
