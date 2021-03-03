import pybullet as p
import pybullet_data
import time as t
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c
from simulation import SIMULATION


simulation = SIMULATION()
# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.setGravity(0,0,-9.8)
# planeId = p.loadURDF("plane.urdf")
# robot = p.loadURDF("body.urdf")
# p.loadSDF("world.sdf")
# pyrosim.Prepare_To_Simulate("body.urdf")
#
# frontLegAngles = c.frontLegAmplitude * np.sin(np.linspace(-c.frontLegFrequency*np.pi+c.frontLegPhaseOffset,
#                                                         c.frontLegFrequency*np.pi+c.frontLegPhaseOffset, num=c.loopRange))
# backLegAngles = c.backLegAmplitude * np.sin(np.linspace(-c.backLegFrequency*np.pi+c.backLegPhaseOffset,
#                                                         c.backLegFrequency*np.pi+c.backLegPhaseOffset, num=c.loopRange))
#
# for i in range(c.loopRange):
#     p.stepSimulation()
#     c.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Back_Leg")
#     c.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Front_Leg")
#
#     pyrosim.Set_Motor_For_Joint( bodyIndex=robot,  jointName="Torso_Back_Leg", controlMode=p.POSITION_CONTROL,
#                                  targetPosition=backLegAngles[i], maxForce=25)
#
#     pyrosim.Set_Motor_For_Joint(bodyIndex=robot, jointName="Torso_Front_Leg", controlMode=p.POSITION_CONTROL,
#                                 targetPosition=frontLegAngles[i], maxForce=25)
#     t.sleep(1/240)
#
#
# np.save("data/backLegSensorValues.npy", c.backLegSensorValues)
# np.save("data/frontLegSensorValues.npy", c.frontLegSensorValues)
# p.disconnect()