from typing import Tuple
import numpy as np
import random
from graph import Graph

def gen_population(graph: Graph, populations: int) -> np.array:
    perms = np.zeros([populations, graph.vertexes_amount + 1], int)
    counter = 0
    # we assume that we start from the first vertex
    vertexes = graph.vertexes[1:]

    while counter < populations:
        permutation = np.random.permutation(vertexes)
        gene = np.append(np.array([0]), permutation)
        gene = np.append(gene, np.array([0]))
        perms[counter] = gene
        counter += 1

    return perms


def population_fitness(g: Graph, p: np.array) -> int:
    s = 0

    for gene in p:
        s += g.route_fitness(gene)

    return s


def crossover(g: Graph, mother_gene: np.array, father_gene: np.array) -> np.array:
    mother_route = mother_gene[1: -1]
    father_route = father_gene[1: -1]

    middle_idx = len(mother_route) // 2

    mother_offspring = mother_route[middle_idx:]

    father_offspring = np.array([vertex for vertex in father_route if vertex not in mother_offspring])

    offspring_route = np.append(father_offspring, mother_offspring)

    return g.complete_route(offspring_route)


def mutate(g: Graph, gene: np.array) -> np.array:
    route = gene[1: -1]

    swap_first_idx = random.randint(1, len(gene) - 3)
    swap_second_idx = random.randint(1, len(gene) - 3)

    while swap_first_idx == swap_second_idx:
        swap_second_idx = random.randint(1, len(gene) - 3)

    route[swap_first_idx], route[swap_second_idx] = route[swap_second_idx], route[swap_first_idx]

    return g.complete_route(route)

def select_parents(population: np.array) -> Tuple[np.array, np.array]:
    mother_idx = np.random.randint(0, len(population) - 1)

    while (father_idx := np.random.randint(0, len(population) - 1)) == mother_idx:
        continue

    return population[mother_idx], population[father_idx]

