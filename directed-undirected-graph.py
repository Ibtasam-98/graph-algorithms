import networkx as nx
import matplotlib.pyplot as plt

# Create an Directed graph
G_directed = nx.DiGraph()
G_directed.add_nodes_from([1,2,3])
G_directed.add_edges_from([(1,2), (2,3), (3,1)])

# Create an Undirected Graph
G_undirected = nx.DiGraph()
G_undirected.add_nodes_from([1,2,3])
G_undirected.add_edges_from([(1,2), (2,3), (3,1)])

# Plot the directed graph
plt.figure(figsize=(12,6))
plt.subplot(121)
nx.draw(G_directed, with_labels=True, arrows=True, font_weight='bold')
plt.title('Directed Graph')

# Plot the undirected Graph
plt.subplot(122)
nx.draw(G_undirected, with_labels=True, arrows=False, font_weight='bold')
plt.title('Directed Graph')

plt.tight_layout()
plt.show()
