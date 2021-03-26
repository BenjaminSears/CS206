import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p
import constants as c

class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        self.motorValues = []
        self.Prepare_To_Act()


    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        self.phaseOffset = c.phaseOffset

        if self.jointName == "Torso_Back_Leg":
            self.frequency = c.frequency/2
        else:
            self.frequency = c.frequency

        self.motorValues = self.amplitude * np.sin(np.linspace(-self.frequency*np.pi+self.phaseOffset,
                                                                self.frequency*np.pi+self.phaseOffset, num=c.loopRange))

    def SET_VALUE(self, robot, desiredAngle):
        pyrosim.Set_Motor_For_Joint(bodyIndex=robot, jointName=self.jointName, controlMode=p.POSITION_CONTROL,
                                    targetPosition=desiredAngle, maxForce=25)

    def Save_Values(self):
        np.save(f"data/{self.jointName}MotorValues.npy", self.motorValues)