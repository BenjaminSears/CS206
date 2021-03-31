import time as t
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c
from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1]
simulation = SIMULATION(directOrGUI)
simulation.RUN()
simulation.Get_Fitness()