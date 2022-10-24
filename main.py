import numpy as np
import random

np.random.seed(42)
random.seed(42)
from graph import Graph
from genetic import gen_population, crossover, mutate, select_parents, population_fitness
import matplotlib.pyplot as plt

plt.figure(figsize=(22, 6))


vertexes_amount = 10
population_amount = 10
mutate_threshold = 0.3
iterations = 200

graph = Graph(vertexes_amount)

population = gen_population(graph, population_amount)
total_fitness_values = [population_fitness(graph, population)]
population_fitness_values = [graph.route_fitness(route) for route in population]
min_fitness_values = [np.min(population_fitness_values)]

for i in range(iterations):
    children = []
    while len(children) <= population_amount:
        mother, father = select_parents(population)
        child = crossover(graph, mother, father)
        if np.random.rand() < mutate_threshold:
            child = mutate(graph, child)
        children.append(child)

    total_fitness = population_fitness(graph, children)
    total_fitness_values.append(total_fitness)
    population_fitness_values = [graph.route_fitness(route) for route in children]
    min_fitness_values.append(np.min(population_fitness_values))

    population = np.array(children)


plt.plot(min_fitness_values)
plt.title("Min Fitness Values")
plt.xticks(np.arange(0, iterations, 10))
plt.grid()
plt.show()