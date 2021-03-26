import time as t
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c
from simulation import SIMULATION

simulation = SIMULATION()
simulation.RUN()
simulation.Get_Fitness()