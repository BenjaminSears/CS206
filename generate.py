import pyrosim.pyrosim as pyrosim
length = 1
width = 1
height = 1

def Create_World(x,y,z):
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
    pyrosim.End()


def Create_Robot(x,y,z):
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[x, y, z], size=[length, width, height])
    pyrosim.End()


Create_World(-3,3,.5)
Create_Robot(0,0,.5)
