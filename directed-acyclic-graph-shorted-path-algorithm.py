import matplotlib.pyplot as plt
import networkx as nx
import heapq

# Topological Sort for DAG
def topological_sort(graph, v, visited, stack):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor[0]]:
            topological_sort(graph, neighbor[0], visited, stack)
    stack.append(v)

# DAG Shortest Path
def dag_shortest_path(graph, source):
    V = len(graph)
    visited = [False] * V
    stack = []

    # Perform topological sorting
    for i in range(V):
        if not visited[i]:
            topological_sort(graph, i, visited, stack)

    dist = [float("inf")] * V
    dist[source] = 0

    # Process vertices in topological order
    while stack:
        u = stack.pop()
        if dist[u] != float("inf"):
            for neighbor in graph[u]:
                v, weight = neighbor
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

    return dist

# Visualizing the graph
def visualize_graph(graph):
    G = nx.DiGraph()
    for u in graph:
        for v, w in graph[u]:
            G.add_edge(u, v, weight=w)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', arrows=True)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()

# Example Graph
graph = {0: [(1, 2), (2, 3)],
         1: [(3, 3)],
         2: [(3, 1)],
         3: []}

# Running the DAG Shortest Path from source 0
source = 0
distances = dag_shortest_path(graph, source)
print(f"Shortest distances from node {source}: {distances}")

visualize_graph(graph)
