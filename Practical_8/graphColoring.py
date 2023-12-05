def is_safe(graph, node, color, c):
    for i in range(len(graph)):
        if graph[node][i] == 1 and color[i] == c:
            return False
    return True

def graph_coloring(graph, num_colors):
    num_nodes = len(graph)
    color = [-1] * num_nodes

    if graph_color_util(graph, num_colors, color, 0):
        print("Solution exists: Following are the assigned colors:")
        for c in color:
            print(c)
    else:
        print("Solution does not exist")

def graph_color_util(graph, num_colors, color, node):
    num_nodes = len(graph)
    if node == num_nodes:
        return True

    for c in range(num_colors):
        if is_safe(graph, node, color, c):
            color[node] = c
            if graph_color_util(graph, num_colors, color, node + 1):
                return True
            color[node] = -1

    return False

graph = [[0, 1, 1, 1],
         [1, 0, 1, 0],
         [1, 1, 0, 1],
         [1, 0, 1, 0]]

num_colors = 3
graph_coloring(graph, num_colors)
