from Projects.solution import *


class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()


    def Evolve(self):
        self.parent.Evaluate()
