import numpy as np
import random

def gen_population(n: int, s: int) -> np.array:
    """ 
    Generating random s routes for n vertexes graph
    Assuming that the first(value=0) point is always a start and an end point
    """

    result = set()

    while len(result) != s:
        route = tuple([0] + random.sample(range(1, n), n - 1) + [0])
        result.add(route)
    
    return np.array(tuple(result))


def build_weights(n: int) -> np.array:
    return np.random.sample([n, n])
