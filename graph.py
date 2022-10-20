import numpy as np
from itertools import pairwise
from functools import reduce


class Graph:
    def __init__(self, n: int):
        self._weights = np.random.randint(0, 20, [n, n])
        self.vertexes_amount = n
        self.vertexes = np.arange(0, n)

    def get_weight(self, v1: int, v2: int) -> int:
        return self._weights[v1, v2]

    def route_fitness(self, route: np.array) -> int:
        edges = pairwise(route)

        def get_weight(edge) -> float:
            return self._weights[edge[0]][edge[1]]

        def accumulator(s, edge):
            return s + get_weight(edge)

        fitness_result = reduce(accumulator, edges, 0)

        return fitness_result

    def get_vertexes(self) -> np.array:
        return self.vertexes

    def complete_route(self, route: np.array) -> np.array:
        gene = np.append(np.array([0]), route)
        gene = np.append(gene, np.array([0]))

        return gene