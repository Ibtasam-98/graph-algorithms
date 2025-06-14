import matplotlib.pyplot as plt
import networkx as nx

# Create an acyclic graph
acyclic_graph = nx.DiGraph()

# Add nodes
acyclic_graph.add_nodes_from([1,2,3,4,5])

# Add edges to create an acyclic structure
acyclic_graph.add_edges_from([(1,2), (1,3), (2,4), (2,5)])

# Visualizr the acyclie graph
pos = nx.spring_layout(acyclic_graph)
nx.draw(acyclic_graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='lightblue', font_size= 8)
plt.show()
