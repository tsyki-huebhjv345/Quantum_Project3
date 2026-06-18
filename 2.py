import networkx as nx
import matplotlib.pyplot as plt

#the Grid (The Graph)
G = nx.Graph()

#add central State Hub
G.add_node("STATE_HUB", color='red')

#add cellular communities
cells = ["Cell_A", "Cell_B", "Cell_C"]

#connect each cell to the central State Hub
for cell in cells:
    G.add_edge("STATE_HUB", cell)

#draw the Grid
#position the nodes using a 'spring layout'
pos = nx.spring_layout(G)

#labels and custom colors
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000)

print("Generating your trapezoidal grid model... Look for the pop-up window!")

plt.show()