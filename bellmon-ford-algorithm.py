import networkx as nx
import matplotlib.pyplot as plt
import sys

class Graph:
    def __init__(self, vertices):
        # Initializes the graph with a specified number of vertices.
        self.V = vertices
        # Stores the graph as a list of edges, where each edge is [u, v, w].
        self.graph = []

    def addEdge(self, u, v, w):
        # Adds an edge to the graph.
        # u: source vertex
        # v: destination vertex
        # w: weight of the edge
        self.graph.append([u, v, w])

    def bellmanFord(self, src):
        # Implements the Bellman-Ford algorithm to find shortest paths from a source vertex.

        # Initialize distances from the source to all other vertices as infinity.
        # The distance to the source itself is 0.
        dist = [float("Inf")] * self.V
        dist[src] = 0

        # Relax all edges V-1 times. A path can have at most V-1 edges.
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                # If a shorter path to v is found through u, update dist[v].
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Check for negative cycles.
        # If we can still relax an edge, it means there's a negative cycle.
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative cycle")
                return None # Return None to indicate a negative cycle

        # Return the array of shortest distances from the source.
        return dist

    def visualizeGraph(self):
        # Visualizes the graph using NetworkX and Matplotlib.
        G = nx.DiGraph() # Create a directed graph

        # Add edges to the NetworkX graph with their weights.
        for u, v, w in self.graph:
            G.add_edge(u, v, weight=w)

        # Use a spring layout for better visualization of nodes.
        pos = nx.spring_layout(G)
        # Draw the nodes and edges.
        nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, arrows=True)
        # Get edge labels (weights) and draw them.
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        # Set the title of the plot.
        plt.title("Bellman-Ford Algorithm")
        # Display the plot.
        plt.show()

# Example usage:
# Create a graph with 5 vertices.
g = Graph(5)
# Add edges with their respective weights.
g.addEdge(0, 1, 6)
g.addEdge(0, 2, 7)
g.addEdge(1, 2, 8)
g.addEdge(1, 3, -4)
g.addEdge(1, 4, 5)
g.addEdge(2, 3, 9)
g.addEdge(2, 4, -3)
g.addEdge(3, 4, 7)

# Set the source node for the Bellman-Ford algorithm.
source_node = 0
# Run the Bellman-Ford algorithm to find shortest distances.
distances = g.bellmanFord(source_node)

# Print the shortest distances if no negative cycle was detected.
if distances is not None:
    print("Shortest distances from source node", source_node, "to all other nodes:")
    for i in range(len(distances)):
        print("Node", i, ":", distances[i])

# Visualize the graph.
g.visualizeGraph()
