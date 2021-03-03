import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import time as t
from world import WORLD
from robot import ROBOT


class SIMULATION:

    def __init__(self):

        self.world = WORLD()
        self.robot = ROBOT()
        # self.physicsClient = p.connect(p.GUI)
        # p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)

    def __del__(self):

        p.disconnect()

    def RUN(self):
        for t in range(100):
            p.stepSimulation()
            #self.robot.SENSE()
            #
            # pyrosim.Set_Motor_For_Joint(bodyIndex=robot, jointName="Torso_Back_Leg", controlMode=p.POSITION_CONTROL,
            #                             targetPosition=backLegAngles[i], maxForce=25)
            #
            # pyrosim.Set_Motor_For_Joint(bodyIndex=robot, jointName="Torso_Front_Leg", controlMode=p.POSITION_CONTROL,
            #                             targetPosition=frontLegAngles[i], maxForce=25)
            t.sleep(1 / 30)