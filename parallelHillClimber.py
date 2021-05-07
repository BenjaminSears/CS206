from solution import *
import constants as c
import numpy as np
import copy


class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        os.system("del tmp*.txt")
        self.nextAvailableID = 0
        self.parents = {}
        for idx in range(0, c.populationSize, 1):
            self.parents[idx] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID+=1

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()

        self.Evaluate(self.children)

        self.Print()

        self.Select()

    def Spawn(self):
        self.children = {}
        for idx in range(0, c.populationSize, 1):
            addParent = copy.deepcopy(self.parents[idx])
            addParent.Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
            self.children[idx] = addParent

    def Mutate(self):
        for child in self.children.values():
            child.Mutate()

    def Select(self):
        for idx in self.parents.keys():
            if self.parents[idx].fitness > self.children[idx].fitness:
                self.parents[idx] = self.children[idx]

    def Print(self):
        print()
        for key in self.parents.keys():
            print(self.parents[key].fitness, self.children[key].fitness)
        print()

    def Show_Best(self):
        lowestSolution = self.parents[0]
        for idx in self.parents.keys():
            if self.parents[idx].fitness < lowestSolution.fitness:
                lowestSolution = self.parents[idx]
        lowestSolution.Start_Simulation("GUI")


    def Evaluate(self, solutions):
        for solution in solutions.values():
            solution.Start_Simulation("DIRECT")
        for solution in solutions.values():
            solution.Wait_For_Simulation_To_End()