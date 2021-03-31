import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import time as t
from world import WORLD
from robot import ROBOT
import constants as c



class SIMULATION:

    def __init__(self, directOrGUI):
        self.directOrGUI = directOrGUI;
        if self.directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        elif self.directOrGUI == "GUI":
            self.physicsClient = p.connect(p.GUI)
        else:
            raise Exception("Invalid directOrGUI value", directOrGUI)

        self.world = WORLD()
        self.robot = ROBOT()
        p.setGravity(0,0,-9.8)

    def __del__(self):

        p.disconnect()

    def RUN(self):
        for step in range(c.loopRange):
            p.stepSimulation()
            self.robot.Sense(step)
            self.robot.Think()
            self.robot.Act()
            if self.directOrGUI == "GUI":
                t.sleep(1.0 / 250)

    def Get_Fitness(self):
        self.robot.Get_Fitness()