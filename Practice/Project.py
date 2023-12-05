import networkx as nx

# Given graph
graph = [
    [3, 0, 0, 0, 0, 2, 0, 3, 0, 0, 0, 0, 0],
    [0, 3, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 2],
    [0, 0, 0, 0, 2, 0, 0, 0, 0, 3, 0, 2, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0],
]

# Convert the adjacency matrix to a NetworkX graph
G = nx.Graph()
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] > 0:
            G.add_edge(i, j, weight=graph[i][j])

# Find the chromatic index (minimum number of colors needed for edge coloring)
chromatic_index = nx.greedy_color(G, strategy='largest_first', interchange=True)

# Print the result
print("Chromatic Index:", max(chromatic_index.values()) + 1)
