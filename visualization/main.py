import csv
from event import event
import matplotlib.pyplot as plt
import networkx as nx

#node, edge, unixtimes
nodes=set()
edges=[]
unixtimes=[]

#data 불러오기 
file=open('visualization/data/data-1000.csv','r')
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
    

#unixtimes.append(0) #시작 시간 추가 
unixtimes.sort() #unixtime 오름차순 정렬
nodes=list(nodes) #node set -> node list 


#visualization

# create a graph
G=nx.Graph()

time_nodes={} #기준 시간축 노드들

time_value=100000 #시간 축 간격 기준, 기준이 너무 크면 오류 

max_unixtime=max(unixtimes)
min_unixtime=min(unixtimes)



time_axis=min_unixtime

#각 시간축마다 노드들 이름 변경하여 추가 
while(time_axis<max_unixtime):
    new_nodes=[]
    for t in range(len(nodes)):
        new_nodes.append(nodes[t]+"-"+str(time_axis))
    time_nodes[time_axis]=new_nodes
    time_axis+=time_value
    


#그래프에 node 추가 
time_axis=min_unixtime
while(time_axis<max_unixtime):
    G.add_nodes_from(time_nodes[time_axis])
    time_axis+=time_value


#그래프에 edge 추가
for edge in edges:
    time_index=int((int(edge.unixtime)-min_unixtime)/time_value)
    if time_index==0:
        G.add_edge(edge.source+"-"+str(min_unixtime),edge.target+"-"+str(min_unixtime+time_value))
    else:
        G.add_edge(edge.source+"-"+str(min_unixtime+(time_index*time_value-time_value)),edge.target+"-"+str(min_unixtime+time_index*time_value))
    

    



# Define a custom layout
pos = {}

x_axis=0
time_axis=min_unixtime

while(time_axis<max_unixtime):
    for index in range(len(time_nodes[time_axis])):
        pos[time_nodes[time_axis][index]]=(x_axis,index)
        
    x_axis+=10000
    time_axis+=time_value
    
# Draw the graph with the custom layout
nx.draw(G,pos,node_size=1)

# Show the plot
plt.show()








##모든 시간을 시간축으로 할 경우 

# Create a graph
# G = nx.Graph()

# #time nodes
# time_nodes={}

# for unixtime in unixtimes:
#     new_nodes=[]
#     for t in range(len(nodes)):
#         new_nodes.append(nodes[t]+"-"+str(unixtime))
#     time_nodes[unixtime]=new_nodes
    



# #insert node
# for unixtime in unixtimes:
#     G.add_nodes_from(time_nodes[unixtime])
    
    
# # Define a custom layout
# pos = {}

# x_axis=0

# for unixtime in unixtimes:
#     for index in range(len(time_nodes[unixtime])):
#         pos[time_nodes[unixtime][index]]=(x_axis,index)

#     x_axis+=10000





# # Draw the graph with the custom layout
# nx.draw(G,pos,node_size=1)

# # Show the plot
# plt.show()
