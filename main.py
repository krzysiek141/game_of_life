import numpy as np


def generate_next_generations(initial_matrix, generations_number):
    generations = []
    current_matrix = np.array(initial_matrix, dtype=bool)

    for _ in range(generations_number):
        current_matrix = get_next_generation(current_matrix)
        generations.append(current_matrix.astype(int).tolist())
    
    return generations

def get_next_generation(matrix):
    m, n = matrix.shape
    next_matrix = matrix.copy()
    for i in range(m):
        for j in range(n):
            alive_neighbors = count_alive_neighbors(matrix, i, j)
            is_alive = matrix[i, j]
            if should_change_state(is_alive, alive_neighbors):
                next_matrix[i, j] = not is_alive

    return next_matrix

def count_alive_neighbors(matrix, i, j):
    alive_neighbors = 0
    m, n = matrix.shape
    for k in range(i - 1, i + 2):
        if k < 0 or k > (m - 1):
            continue
        for l in range(j - 1, j + 2):
            if l < 0 or l > (n - 1):
                continue
            if matrix[k, l] == True and not (k == i and l == j):
                alive_neighbors += 1

    return alive_neighbors

def should_change_state(is_alive, alive_neighbors):
    if is_alive:
        return alive_neighbors < 2 or alive_neighbors > 3
    else:
        return alive_neighbors == 3