import csv
from event import event
import matplotlib.pyplot as plt
import networkx as nx

#node, edge, unixtimes
nodes=set()
edges=[]
unixtimes=[]

#data 불러오기 
file=open('graph visualization/data/data-1000.csv','r')
lines=csv.reader(file)

for line in lines:
    #coloum 제거
    if line[0]=="source":
        continue
    
    #node 추가
    nodes.add(line[0])
    nodes.add(line[1])
    
    #unixtime 추가
    unixtimes.append(int(line[2]))
    
    #edge 추가 
    label=line[0]+"|"+line[1]+"|"+line[2]
    edges.append(event(label,line[0],line[1],line[2]))
    

unixtimes.sort() #unixtime 오름차순 정렬

#visualization

# Create a graph
G = nx.Graph()

# Add some nodes to the graph
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8])

# Add some edges to the graph
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (4, 6), (5, 7), (6, 8), (7, 8)])

# Define a custom layout
pos = {1: (0, 0), 2: (1, 1), 3: (-1, 1), 4: (2, 0), 5: (3, 1), 6: (2, -1), 7: (4, 1), 8: (4, -1)}

# Draw the graph with the custom layout
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=14, font_weight='bold')

# Show the plot
plt.show()
