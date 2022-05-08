import numpy as np
import operator
from itertools import pairwise
from functools import reduce

def calc_route_fitness(route: np.array, weights: np.array) -> float:
    edges = pairwise(route)

    def get_weight(edge) -> float:
        return weights[edge[0]][edge[1]]
    def accumulator(s, edge):
        return s + get_weight(edge)

    fitness_result = reduce(accumulator, edges, 0)

    return fitness_result


def calc_population_fitness(population: np.array, weights: np.array) -> float:
    fitness_values = map(lambda route: calc_route_fitness(route, weights), population)

    total_fitness = reduce(operator.add, fitness_values)

    return total_fitness
