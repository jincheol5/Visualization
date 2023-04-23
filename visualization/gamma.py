import csv
import pandas as pd
from event import event


##데이터 불러오기 
#node, edge, unixtimes
nodes=set()
edges=[]
unixtimes=set()

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
    unixtimes.add(int(line[2]))
    
    #edge 추가 
    label=line[0]+"|"+line[1]+"|"+line[2]
    edges.append(event(label,line[0],line[1],line[2]))
    

#unixtimes.append(0) #시작 시간 추가 
unixtimes=list(unixtimes)#unixtime 리스트 변환
unixtimes.sort()#오름차순 정렬

nodes=list(nodes) #node set -> node list 


##gamma table 생성
#1. 각 노드에 대한 gamma table 생성 

gammatables={}

for node in nodes:
    
    #2차원 table 생성
    new_table=[[0 for i in range(len(unixtimes))] for i in range(len(nodes))]
    for node in nodes:
        new_table_df=pd.DataFrame(new_table,index=[node for node in nodes],columns=[unixtime for unixtime in unixtimes])
        
    #각 node key에 value 값으로 저장 
    gammatables[node]=new_table_df
    