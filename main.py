from fitness import calc_population_fitness
from random_map import gen_population, build_weights

vertexes_amount = 10
population_amount = 10
population = gen_population(vertexes_amount, population_amount)
weights = build_weights(population_amount)

fitness_value = calc_population_fitness(population, weights)

print(fitness_value)
