from __future__ import division
from helpers import *
from numpy import random

class Graph():
    def __init__(self, g):
        self.g = g
        self.vertexes = np.arange(len(self.g))

    def fitness_function(self, genotype):
        res = 0
        for i in np.arange(len(genotype) - 2):
            res += self.g[i, i+1]
        return res

    def selection(self, generation):
        gen_len = len(generation)

        first_gen = generation[int(gen_len * random.random())]
        second_gen = generation[int(gen_len * random.random())]

        return first_gen if self.fitness_function(first_gen) > self.fitness_function(second_gen) else second_gen
