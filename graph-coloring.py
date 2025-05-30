import matplotlib.pyplot as plt
import networkx as nx
from typing import Dict, List


def greedy_coloring(graph: nx.Graph) -> Dict[int, int]:
    """
    Perform greedy coloring for the given graph
    Args:
    graph (nx.Graph): The graph to be colored

    :return
    Dict[int, int]: A dictionary where keys are nodes and values are color.
    """
    coloring = {}
    for node in graph.nodes():
        avaliable_colors = set(range(len(graph.nodes())))
        for neighbor in graph.neighbors(node):
            if neighbor in coloring:
                avaliable_colors.discard(coloring[neighbor])
            coloring[node] = min(avaliable_colors)
    return coloring


def visualize_graph_coloring(graph: nx.Graph, coloring: Dict[int, int]):
    """
    visualize the graph with colors assigned to nodes
    :arg
    graph (nx.Graph): The graph to be visualized.
    coloring (Dict[int, int]): A dictionary where keys are nodes and values
    are color
    """
    pos = nx.spring_layout(graph)
    colors = [coloring[node] for node in graph.nodes()]
    nx.draw(graph, pos, with_labels=True, node_color=colors, node_size=800,
            cmap=plt.cm.rainbow)
    plt.show()


# Example
if __name__ == "__main__":
    # Create a graph
    G = nx.Graph()
    edges: List[tuple] = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4)]
    G.add_edges_from(edges)

    # Perform a greedy coloring
    coloring = greedy_coloring(G)
    print("Node Coloring", coloring)

    # Visualize the graph coloring
    visualize_graph_coloring(G, coloring)
