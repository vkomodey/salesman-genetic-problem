import numpy as np


def crossover_coord(vec_len, p_c):
    for i in range(vec_len):
        r = random()
        if r > p_c:
            return i

    return vec_len - 1


def random():
    return np.random.rand()


def generate_individual(length, start_index):
    vec = np.arange(0, length)
    vec[0], vec[start_index] = vec[start_index], vec[0]
    vec[-1] = start_index
    np.random.shuffle(vec[1:-1])
    return vec


def init_first_generation(vec_length, ind_amount, start_index):
    generation = np.empty([ind_amount, vec_length + 1])

    for i in range(ind_amount):
        generation[i] = generate_individual(vec_length + 1, start_index)

    return generation


def random_int(length):
    return np.random.random_integers(0, length - 1)


def crossover(ksi, nu):
    vec_len = len(ksi)
    # calculate crossover indices
    p1 = random_int(vec_len - 1)
    p2 = random_int(vec_len - 1)

    if p1 > p2:
        p1, p2 = p2, p1
    print("p1={}, p2={}".format(p1, p2))

    p1 = 1
    p2 = 5
    crossed_ksi = np.empty(vec_len)
    crossed_nu = np.empty(vec_len)
    # fill crossed vectors with -1, we have no negative vertexes, so it would be easy
    # to compare occurrence of other elements in current array
    crossed_ksi.fill(-1)
    crossed_nu.fill(-1)

    # fill start and last gene as first elem in ksi(no matter, ksi or nu, they are equal)
    # start point is always the same for all generations and all genotypes
    start_point = ksi[0]
    crossed_ksi[0] = crossed_ksi[-1] = crossed_nu[0] = crossed_nu[-1] = start_point

    # Fill middle part
    crossed_ksi[p1:p2] = nu[p1:p2]
    crossed_nu[p1:p2] = ksi[p1:p2]

    # calculate other empty parts, where we wanna to do crossover
    first_part = np.arange(1, p1)
    second_part = np.arange(p2, vec_len)
    indices = np.concatenate((first_part, second_part), axis=0)

    for i in indices:
        if ksi[i] not in crossed_ksi and nu[i] not in crossed_nu:
            crossed_ksi[i] = ksi[i]
            crossed_nu[i] = nu[i]
        else:
            crossed_ksi[i] = nu[i]
            crossed_nu[i] = ksi[i]

    yield crossed_ksi
    yield crossed_nu


def mutate(individual, p_m):
    vec_len = len(individual)
    mutated = np.empty(vec_len)
    r = random()

    for i in range(vec_len):
        if r > p_m:
            mutated[i] = 0 if individual[i] == 1 else 1
        else:
            mutated[i] = individual[i]

    return mutated
