from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import time

x = []
y = []

# 4 CITIES SAME STATE
cities = ['Nagpur', 'Akola', 'Mumbai', 'Nashik']

geolocator = Nominatim(user_agent="Location")

graph = []


def kruskal(graph):
    V = len(graph)
    edges = []

    # Create a list of edges with weights
    for i in range(V):
        for j in range(i + 1, V):
            if graph[i][j] != 0:
                edges.append((i, j, graph[i][j]))

    # Sort the edges by weight
    edges.sort(key=lambda x: x[2])

    # Initialize parent and rank arrays for Union-Find
    parent = [i for i in range(V)]
    rank = [0] * V

    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]

    def union(u, v):
        root_u = find(u)
        root_v = find(v)
        if root_u != root_v:
            if rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            elif rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            else:
                parent[root_v] = root_u
                rank[root_u] += 1

    minimum_spanning_tree = []
    mst_weight = 0

    # Process edges in ascending order of weight
    for edge in edges:
        u, v, weight = edge
        if find(u) != find(v):
            minimum_spanning_tree.append(edge)
            mst_weight += weight
            union(u, v)

    return minimum_spanning_tree, mst_weight


for i in range(4):
    city = geolocator.geocode(cities[i])
    li = []
    for j in range(4):
        if i == j:
            li.append(float('inf'))
        else:
            cit = geolocator.geocode(cities[j])
            city1 = (city.latitude, city.longitude)
            city2 = (cit.latitude, cit.longitude)
            distance = geodesic(city1, city2).km
            li.append(distance)
    graph.append(li)

print(graph)

# Find the Minimum Spanning Tree and its weight
start=time.perf_counter()
mst, mst_weight = kruskal(graph)
end= time.perf_counter()
timetaken=end-start
x.append(timetaken)

# Print the Minimum Spanning Tree edges and its weight
print("Minimum Spanning Tree Edges:")
for edge in mst:
    print(edge)

print("Minimum Spanning Tree Weight:", mst_weight)


# 4 CITY OUTSIDE STATE
cities = ['Nagpur', 'Haryana', 'Kerala', 'Katol']

graph=[]
for i in range(4):
    city = geolocator.geocode(cities[i])
    li = []
    for j in range(4):
        if i == j:
            li.append(0)
        else:
            cit = geolocator.geocode(cities[j])
            city1 = (city.latitude, city.longitude)
            city2 = (cit.latitude, cit.longitude)
            distance = geodesic(city1, city2).km
            li.append(distance)
    graph.append(li)

print(graph)

# Find the Minimum Spanning Tree and its weight
start=time.perf_counter()
mst, mst_weight = kruskal(graph)
end= time.perf_counter()
timetaken=end-start
y.append(timetaken)


# Print the Minimum Spanning Tree edges and its weight
print("Minimum Spanning Tree Edges:")
for edge in mst:
    print(edge)

print("Minimum Spanning Tree Weight:", mst_weight)



# FOR 5 CITIES (SAME STATE)
cities = ['Nagpur', 'Akola', 'Mumbai', 'Nashik','Pune']

graph=[]
for i in range(5):
    city = geolocator.geocode(cities[i])
    li = []
    for j in range(5):
        if i == j:
            li.append(0)
        else:
            cit = geolocator.geocode(cities[j])
            city1 = (city.latitude, city.longitude)
            city2 = (cit.latitude, cit.longitude)
            distance = geodesic(city1, city2).km
            li.append(distance)
    graph.append(li)

print(graph)

# Find the Minimum Spanning Tree and its weight
start=time.perf_counter()
mst, mst_weight = kruskal(graph)
end= time.perf_counter()
timetaken=end-start
x.append(timetaken)

# Print the Minimum Spanning Tree edges and its weight
print("Minimum Spanning Tree Edges:")
for edge in mst:
    print(edge)

print("Minimum Spanning Tree Weight:", mst_weight)


# FOR 5 CITIES (DIFFERENT STATE)
cities = ['Nagpur', 'Haryana', 'Kerala', 'Katol','Indore']

graph=[]
for i in range(5):
    city = geolocator.geocode(cities[i])
    li = []
    for j in range(5):
        if i == j:
            li.append(0)
        else:
            cit = geolocator.geocode(cities[j])
            city1 = (city.latitude, city.longitude)
            city2 = (cit.latitude, cit.longitude)
            distance = geodesic(city1, city2).km
            li.append(distance)
    graph.append(li)

print(graph)

# Find the Minimum Spanning Tree and its weight
start=time.perf_counter()
mst, mst_weight = kruskal(graph)
end= time.perf_counter()
timetaken=end-start
y.append(timetaken)

# Print the Minimum Spanning Tree edges and its weight
print("Minimum Spanning Tree Edges:")
for edge in mst:
    print(edge)

print("Minimum Spanning Tree Weight:", mst_weight)



# FOR 6 CITIES (SAME STATE)
cities = ['Nagpur', 'Akola', 'Mumbai', 'Nashik','Pune','Amravati']

graph=[]
for i in range(6):
    city = geolocator.geocode(cities[i])
    li = []
    for j in range(6):
        if i == j:
            li.append(0)
        else:
            cit = geolocator.geocode(cities[j])
            city1 = (city.latitude, city.longitude)
            city2 = (cit.latitude, cit.longitude)
            distance = geodesic(city1, city2).km
            li.append(distance)
    graph.append(li)

print(graph)

# Find the Minimum Spanning Tree and its weight
start=time.perf_counter()
mst, mst_weight = kruskal(graph)
end= time.perf_counter()
timetaken=end-start
x.append(timetaken)

# Print the Minimum Spanning Tree edges and its weight
print("Minimum Spanning Tree Edges:")
for edge in mst:
    print(edge)

print("Minimum Spanning Tree Weight:", mst_weight)

# FOR 6 CITIES (DIFFERENT STATE)
cities = ['Nagpur', 'Haryana', 'Kerala', 'Katol','Indore','Kolkata']

graph=[]
for i in range(6):
    city = geolocator.geocode(cities[i])
    li = []
    for j in range(6):
        if i == j:
            li.append(0)
        else:
            cit = geolocator.geocode(cities[j])
            city1 = (city.latitude, city.longitude)
            city2 = (cit.latitude, cit.longitude)
            distance = geodesic(city1, city2).km
            li.append(distance)
    graph.append(li)

print(graph)

# Find the Minimum Spanning Tree and its weight
start=time.perf_counter()
mst, mst_weight = kruskal(graph)
end= time.perf_counter()
timetaken=end-start
y.append(timetaken)

# Print the Minimum Spanning Tree edges and its weight
print("Minimum Spanning Tree Edges:")
for edge in mst:
    print(edge)

print("Minimum Spanning Tree Weight:", mst_weight)

print('\n\n\n',x)
print(y)


import matplotlib.pyplot as plt

# Data
data = [
    x,
    y
]

# Create the plot
plt.figure(figsize=(10, 6))

plt.plot(data[0], label='Within State', marker='o', linestyle='-')

plt.plot(data[1], label='Outside state', marker='x', linestyle='-')

plt.title('Data Analysis Plot')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.grid(True)

plt.show()