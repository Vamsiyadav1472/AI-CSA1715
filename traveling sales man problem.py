from itertools import permutations
def tsp_brute_force(dist_matrix):
    n = len(dist_matrix)
    min_path = None
    min_cost = float('inf')
    for perm in permutations(range(1, n)):
        path = [0] + list(perm) + [0]
        cost = sum(dist_matrix[path[i]][path[i+1]] for i in range(n))
        if cost < min_cost:
            min_cost = cost
            min_path = path
    return min_path, min_cost
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
path, cost = tsp_brute_force(dist)
print("Shortest path:", path)
print("Minimum cost:", cost)
