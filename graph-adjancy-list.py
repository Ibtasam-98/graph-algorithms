import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        # Adding edge from vertex u to vertex v
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

        # Adding edge from vertex v to vertex u (assuming an undirected graph)
        if v in self.graph:
            self.graph[v].append(u)
        else:
            self.graph[v] = [u]

    def visualize(self):
        G = nx.Graph()
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                G.add_edge(vertex, neighbor)

        pos = nx.spring_layout(G)

        # Draw the graph
        fig, ax = plt.subplots(figsize=(12, 5), nrows=1, ncols=2)

        nx.draw(G, pos, with_labels=True, font_weight='bold',
                node_size=700, node_color='skyblue',
                font_color='black', font_size=10,
                edge_color='gray', linewidths=1,
                alpha=0.7, ax=ax[0])
        ax[0].set_title('Graph Visualization')

        # Display the adjacency list
        adjacency_list = "\nAdjacency List:\n"
        for vertex in self.graph:
            adjacency_list += f"{vertex}: {', '.join(map(str, self.graph[vertex]))}\n"

        ax[1].text(0, 0.5, adjacency_list, fontsize=10, va='center', ha='left')
        ax[1].axis('off')  # Turn off the axis for the second subplot

        plt.show()

# Example graph
my_graph = Graph()
my_graph.add_edge(1,2)
my_graph.add_edge(1,3)
my_graph.add_edge(2,3)
my_graph.add_edge(3,4)

my_graph.visualize()
