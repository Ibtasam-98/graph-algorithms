import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        # Initialize the graph using an adjacency list (dictionary)
        self.graph = {}

    def add_edge(self, u, v):
        # Add an edge from u to v. If u doesn't exist, create it.
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

        # For an undirected graph, also add an edge from v to u.
        if v in self.graph:
            self.graph[v].append(u)
        else:
            self.graph[v] = [u]

    def visualize(self):
        # Create a NetworkX graph from our adjacency list
        G = nx.Graph()
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                G.add_edge(vertex, neighbor)

        # Generate node positions for visualization
        pos = nx.spring_layout(G)

        # Set up a figure with two subplots: one for the graph, one for the adjacency list
        fig, ax = plt.subplots(figsize=(12, 5), nrows=1, ncols=2)

        # Draw the graph on the first subplot
        nx.draw(G, pos, with_labels=True, font_weight='bold',
                node_size=700, node_color='skyblue',
                font_color='black', font_size=10,
                edge_color='gray', linewidths=1,
                alpha=0.7, ax=ax[0])
        ax[0].set_title('Graph Visualization')

        # Prepare and display the adjacency list on the second subplot
        adjacency_list = "\nAdjacency List:\n"
        for vertex in self.graph:
            adjacency_list += f"{vertex}: {', '.join(map(str, self.graph[vertex]))}\n"

        ax[1].text(0, 0.5, adjacency_list, fontsize=10, va='center', ha='left')
        ax[1].axis('off') # Hide axes for the text subplot

        plt.show()

# Example usage
my_graph = Graph()
my_graph.add_edge(1,2)
my_graph.add_edge(1,3)
my_graph.add_edge(2,3)
my_graph.add_edge(3,4)

my_graph.visualize()
