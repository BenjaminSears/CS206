import numpy as np

loopRange = 1500
backLegSensorValues = np.zeros(loopRange)
frontLegSensorValues = np.zeros(loopRange)
amplitude = np.pi/4.15
frequency = 8.0
phaseOffset = 0

backLegAmplitude = np.pi/4.15
backLegFrequency = 8.0
backLegPhaseOffset = 0

frontLegAmplitude = np.pi/7
frontLegFrequency = 7.9
frontLegPhaseOffset = np.pi/2.8

# Hill climber
numberOfGenerations = 10

# Parallel Hill Climber
populationSize = 10
