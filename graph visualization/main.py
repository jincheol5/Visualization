import networkx as nx
from event import Event
import matplotlib.pyplot as plt
from visualization import draw_graph,draw_bipartite

events=[] #event class list  
nodes=set() #node list  

f = open("data/data-10.txt", 'r')

lines=f.readlines()


for line in lines:
    dt=line.split(' ')
    events.append(Event(dt[0],dt[1],dt[2])) #event class list에 data 입력
    
    #nodes에 node들 입력 (중복 제거)
    nodes.add(dt[0]) 
    nodes.add(dt[1])

events=sorted(events,key=lambda x:x.unix_time) #event들을 unix time 기준으로 오름차순 정렬 
nodes=list(nodes) #node set을 list로 변환  



f.close()

draw_bipartite(nodes,events)


