import pyrosim.pyrosim as pyrosim
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
    pyrosim.End()


Create_World()
Generate_Body()
Generate_Brain()
