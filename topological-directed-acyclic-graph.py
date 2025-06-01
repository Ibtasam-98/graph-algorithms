import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def kahn_topologicak_sort(graph):
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    queue = deque([u for u in graph if in_degree[u] == 0])
    topological_order = []

    while queue:
        u = queue.popleft()
        topological_order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    if len(topological_order) == len(graph):
        return topological_order
    else:
        return [] # Graph has a cycle

def draw_graph(graph):
    G = nx.DiGraph()
    for node, neighbors in graph.items():
        G.add_node(node)
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, arrows=True)
    plt.title('Directed Acyclic Graph')
    plt.show()

def visualize_topological_sort(graph, topological_order):
    G = nx.DiGraph()
    for node, neighbors in graph.items():
        G.add_node(node)
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, arrows=True)
    plt.title('Topological Sorting')
    plt.show()

def main():
    graph = {
        'A': ['C'],
        'B': ['C', 'D'],
        'C': ['E'],
        'D': ['F'],
        'E': ['F'],
        'F': []
    }
    print("Initial Directed Graph:")
    draw_graph(graph)
    sorted_order = kahn_topologicak_sort(graph)
    if sorted_order:
        print("Topological Sorting Order :", sorted_order)
        visualize_topological_sort(graph, sorted_order)
    else:
        print("Gprh containes a cycle, cannot perform topological sorting")

if __name__ == "__main__":
    main()
























