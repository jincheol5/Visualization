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
    edges.append(event(label,line[0],line[1],int(line[2])))
    

#unixtimes.append(0) #시작 시간 추가 
unixtimes=list(unixtimes)#unixtime 리스트 변환
unixtimes.sort()#오름차순 정렬

nodes=list(nodes) #node set -> node list 


##gamma table 생성
#0. 이벤트 발생 시간 
event_time=0

#unixtime 정리
event_unixtimes=[] #event 발생 이후의 unixtimes

if event_time not in unixtimes:
    event_unixtimes.append(event_time)


for unixtime in unixtimes:
    if unixtime>=event_time:
        event_unixtimes.append(unixtime)
        
#edge event 정리
event_edges=[] #event 발생 이후의 edges


for edge in edges:
    if edge.unixtime>=event_time:
        event_edges.append(edge)



#1. 각 노드에 대한 gamma table 생성 
gammatables={} #gamma table 저장 dictionary





for node in nodes:
    
    #2차원 table 생성
    new_table=[[0 for i in range(len(unixtimes))] for i in range(len(nodes))]
    for node in nodes:
        new_table_df=pd.DataFrame(new_table,index=[node for node in nodes],columns=[unixtime for unixtime in unixtimes])
        
    #각 node key에 value 값으로 저장 
    gammatables[node]=new_table_df
    

for key in gammatables.keys():
    for index in len(nodes):
        for unixtime_index in len(event_unixtimes):
            if nodes[index]==key:
                gammatables[key].loc[index,event_time]
            else:
                gammatables[key].loc[index,0]
                
for key in gammatables.keys():
    print(gammatables[key])
    break
        