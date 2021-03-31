from solution import *
import constants as c
import copy


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.nextAvailableID = 0
        self.parents = {}
        for idx in range(0, c.populationSize, 1):
            self.parents[idx] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID+=1


    def Evolve(self):
        for solution in self.parents.values():
            solution.Evaluate("GUI")
        # for currentGeneration in range(c.numberOfGenerations):
        #     self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()

        self.child.Evaluate("DIRECT")

        self.Print()

        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        self.child.Set_ID()
        self.nextAvailableID+=1

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def Print(self):
        print(self.parent.fitness, self.child.fitness)

    def Show_Best(self):
        # self.parent.Evaluate("GUI")
        pass