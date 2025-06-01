import networkx as nx
import matplotlib.pyplot as plt

# create an unweighted graph
unweighted_graph = nx.Graph()
unweighted_graph.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

# create an weighted graph
weighted_graph = nx.Graph()
weighted_graph.add_edges_from( [(1, 2, {'weight': 2}), (2, 3, {'weight': 1.5}), (3, 4, {'weight': 3}), (4, 1, {'weight': 2})])

# draw unweighted graph
plt.subplot(121)
nx.draw(unweighted_graph, with_labels=True, font_weight='bold')
plt.title('Unweighted Graph')

# Draw weighted graph
plt.subplot(122)
pos = nx.spring_layout(weighted_graph)  # position for all nodes
nx.draw(weighted_graph, pos, with_labels=True, font_weight='bold')
labels = nx.get_edge_attributes(weighted_graph, 'weight')
nx.draw_networkx_edge_labels(weighted_graph, pos, edge_labels=labels)
plt.title('Weighted Graph')

plt.show()
