from __future__ import division
import numpy as np
import time
import matplotlib.pyplot as plt
from numpy import  max, loadtxt
from helpers import init_first_generation, mutate, crossover
from generate_random_graph import generate_random_graph
from graph import Graph
from pprint import pprint
from collections import Counter


print = pprint


start_time = time.time()

# Initial params
# t - iteration maximum
tmax = 100
# N - individuals amount in generation.
N = 100

graph_size = 10

graph = Graph(generate_random_graph(graph_size))
# loaded_matrix = np.loadtxt('graph.txt', dtype=int)
# graph = Graph(loaded_matrix)

l = len(graph.g)

start_index = np.random.random_integers(0, l)
current_generation = init_first_generation(l, N, start_index)

# first_ancestor = graph.selection(current_generation)
# second_ancestor = graph.selection(current_generation)

first_ancestor = np.array([ 9.,  5.,  0.,  2.,  1.,  3.,  8.,  4.,  6.,  7.,  9.])
second_ancestor = np.array([ 9.,  8.,  4.,  2.,  7.,  6.,  1.,  3.,  0.,  5.,  9.])

crossed_first_ancestor, crossed_second_ancestor = crossover(first_ancestor, second_ancestor)

print(crossed_first_ancestor)
print(crossed_second_ancestor)
print((Counter(crossed_first_ancestor) - Counter(set(crossed_first_ancestor))).keys())
# results = np.empty(tmax)

# for t in range(tmax):
#     print(t)
#     next_generation = np.empty([N, l])
#
#     for k in range(N // 2):
#         first_ancestor = graph.selection(current_generation)
#         second_ancestor = graph.selection(current_generation)
#
#         crossed_first_ancestor, crossed_second_ancestor = crossover(first_ancestor, second_ancestor)
#
#         mutated_first_ancestor = mutate(crossed_first_ancestor)
#         mutated_second_ancestor = mutate(crossed_second_ancestor)
#
#         next_generation[2*k - 1] = mutated_first_ancestor
#         next_generation[2*k] = mutated_second_ancestor
#
#     current_generation = next_generation
#     results[t] = max([graph.fitness_function(geno) for geno in current_generation])
#
# plt.ylabel('incision value')
# plt.xlabel('time')
# ll = plt.plot(np.arange(tmax), results)
#
# plt.show()

print("---- %s seconds " % (time.time() - start_time))
