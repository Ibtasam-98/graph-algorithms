import networkx as nx
import matplotlib.pyplot as plt
import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellmanFord(self, src):
        dist = [float("Inf")] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Check for negative cycles
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative cycle")
                return

        return dist

    def visualizeGraph(self):
        G = nx.DiGraph()
        for u, v, w in self.graph:
            G.add_edge(u, v, weight=w)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, arrows=True)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.title("Bellman-Ford Algorithm")
        plt.show()

# Example
g = Graph(5)
g.addEdge(0, 1, 6)
g.addEdge(0, 2, 7)
g.addEdge(1, 2, 8)
g.addEdge(1, 3, -4)
g.addEdge(1, 4, 5)
g.addEdge(2, 3, 9)
g.addEdge(2, 4, -3)
g.addEdge(3, 4, 7)

source_node = 0
distances = g.bellmanFord(source_node)
print("Shortest distances from source node", source_node, "to all other nodes:")
for i in range(len(distances)):
    print("Node", i, ":", distances[i])


g.visualizeGraph()
