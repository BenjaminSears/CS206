import pybullet as p
import pybullet_data
import time as t
import pyrosim.pyrosim as pyrosim
import numpy as np
import math
import random as r

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robot = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate("body.urdf")

loopRange = 1000
amplitude = np.pi/4
frequency = 1
phaseOffset = 0
backLegSensorValues = np.zeros(loopRange)
frontLegSensorValues = np.zeros(loopRange)
targetAngles = np.linspace(-np.pi/4.0, np.pi/4.0, loopRange)
np.save("data/targetAngles.npy", targetAngles)

# for j in range(len(targetAngles)):
#     targetAngles[j] = amplitude * np.sin(frequency * j + phaseOffset)


for i in range(loopRange):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Back_Leg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Front_Leg")

    pyrosim.Set_Motor_For_Joint( # Back leg

        bodyIndex=robot,

        jointName="Torso_Back_Leg",

        controlMode=p.POSITION_CONTROL,

        targetPosition=targetAngles[i],

        maxForce=10)

    pyrosim.Set_Motor_For_Joint( # Front leg

        bodyIndex=robot,

        jointName="Torso_Front_Leg",

        controlMode=p.POSITION_CONTROL,

        targetPosition=targetAngles[i],

        maxForce=10)
    t.sleep(1/240)


np.save("data/backLegSensorValues.npy", backLegSensorValues)
np.save("data/frontLegSensorValues.npy", frontLegSensorValues)
p.disconnect()