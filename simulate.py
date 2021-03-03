import time as t
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c
from simulation import SIMULATION

simulation = SIMULATION()
simulation.RUN()

#
# frontLegAngles = c.frontLegAmplitude * np.sin(np.linspace(-c.frontLegFrequency*np.pi+c.frontLegPhaseOffset,
#                                                         c.frontLegFrequency*np.pi+c.frontLegPhaseOffset, num=c.loopRange))
# backLegAngles = c.backLegAmplitude * np.sin(np.linspace(-c.backLegFrequency*np.pi+c.backLegPhaseOffset,
#                                                         c.backLegFrequency*np.pi+c.backLegPhaseOffset, num=c.loopRange))
#
# np.save("data/backLegSensorValues.npy", c.backLegSensorValues)
# np.save("data/frontLegSensorValues.npy", c.frontLegSensorValues)