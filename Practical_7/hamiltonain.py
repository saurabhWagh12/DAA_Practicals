def is_valid(v, pos, path, graph):
    if not graph[path[pos - 1]][v]:
        return False

    if v in path:
        return False

    return True

def hamiltonian_util(graph, path, pos, cycles):
    n = len(graph)

    if pos == n:
        if graph[path[pos - 1]][path[0]]:
            cycles.append(path[:])
        return

    for v in range(n):
        if is_valid(v, pos, path, graph):
            path[pos] = v

            hamiltonian_util(graph, path, pos + 1, cycles)

            path[pos] = -1

def find_hamiltonian_cycles(graph):
    n = len(graph)
    path = [-1] * n
    path[0] = 0  
    cycles = []
    hamiltonian_util(graph, path, 1, cycles)

    return cycles

# Sample adjacency matrix
adjacency_matrix = [
    [0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1],
    [0, 1, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 0, 1, 0, 1, 0]
]

cycles = find_hamiltonian_cycles(adjacency_matrix)

if cycles:
    print("Hamiltonian Cycles:")
    for cycle in cycles:
        print(cycle)
else:
    print("No Hamiltonian Cycles found")
