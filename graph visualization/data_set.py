import pandas as pd 
from event import Event


class data_set:
    
    def __init__(self,file_name):
        
        self.events=[] #event class list  
        self.nodes=set() #node list  
        self.file=open("data/"+file_name, 'r')
        
        lines=self.file.readlines()
        
        self.file.close()

        for line in lines:
            dt=line.split(' ')
            self.events.append(Event(dt[0],dt[1],dt[2].replace("\n", ""))) #event class list에 data 입력

            #nodes에 node들 입력 (중복 제거)
            self.nodes.add(dt[0]) 
            self.nodes.add(dt[1])

        self.events=sorted(self.events,key=lambda x:x.unix_time) #event들을 unix time 기준으로 오름차순 정렬
        self.nodes=list(self.nodes) #node set을 list로 변환  
        
        
    def get_dataframe(self):
        
        events_dic={
            'source':[],
            'target':[],
            'unix_time':[]
        }
        
        for event in self.events:
            events_dic['source'].append(event.source)
            events_dic['target'].append(event.target)
            events_dic['unix_time'].append(event.unix_time)
            
        return pd.DataFrame(events_dic)
    
    