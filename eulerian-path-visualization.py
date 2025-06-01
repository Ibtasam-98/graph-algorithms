import matplotlib.pyplot as plt
import networkx as nx

# Create a graph
G = nx.Graph()

# Add edges to the graph
edges = [(0,1), (1,2), (2,3), (3,0), (0,2)]
G.add_edges_from(edges)

# Check for Eulerian Circuit and Path
is_eulerian = nx.is_eulerian(G)
eulerian_path = list(nx.eulerian_circuit(G)) \
    if is_eulerian else list(nx.eulerian_path(G))

# Extract nodes from the edges to highlight the path
path_Edges = [(u, v) for u, v in eulerian_path]

# Visualize the graph and highlight the Eulerian Path
pos = nx.spring_layout(G)
nx.draw(G,pos, with_labels=True,
                node_color='lightblue', edge_color='gray',
                node_size=500, font_size=15)
nx.draw_networkx_edges(G, pos, edgelist=path_Edges,
                       edge_color='red', width=2)
plt.title("Eulerian Circuit" if is_eulerian else "Eulerian Path")
plt.show()

# Output
print("Eulerian Path/Circuit: ", eulerian_path)
