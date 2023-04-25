import csv
from event import event
import matplotlib.pyplot as plt
import networkx as nx
from gamma import Gamma

#node, edge, unixtimes
nodes=set()
edges=[]
unixtimes=[]

#data 불러오기 
file=open('visualization/data/data-10.csv','r')
lines=csv.reader(file)



for line in lines:
    #coloum 제거
    if line[0]=="source":
        continue
    
    #node 추가
    nodes.add(line[0].strip())
    nodes.add(line[1].strip())
    
    #unixtime 추가
    unixtimes.append(int(line[2]))
    
    #edge 추가 
    label=line[0]+"|"+line[1]+"|"+line[2]
    edges.append(event(label,line[0].strip(),line[1].strip(),line[2].strip()))
    

unixtimes.sort() #unixtime 오름차순 정렬
nodes=list(nodes) #node set -> node list 

mygamma=Gamma(nodes,edges,unixtimes,1082040961)

mygamma.reset_gamma()
mygamma.tR()

print(mygamma.gammatables["6"])

