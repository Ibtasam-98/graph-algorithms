import heapq
import networkx as nx
import matplotlib.pyplot as plt


def dijkstra(graph, start):
    priority_queue = [(0, start)]
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    G = nx.Graph(graph)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                G.add_edge(current_vertex, neighbor, weight=weight)

    return distances, G


# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
result, visualization_graph = dijkstra(graph, start_vertex)

# Visualize the graph
pos = nx.spring_layout(visualization_graph)
edge_labels = nx.get_edge_attributes(visualization_graph, 'weight')
nx.draw(visualization_graph, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10)
nx.draw_networkx_edge_labels(visualization_graph, pos, edge_labels=edge_labels)
plt.title(f"Dijkstra's Algorithm - Shortest Distances from {start_vertex}")

# Print the result below the graph
plt.figtext(0.5, 0.02, f"Shortest distances from {start_vertex}: {result}", ha='center', va='center', fontsize=10)

# show the graph and result
plt.show()
