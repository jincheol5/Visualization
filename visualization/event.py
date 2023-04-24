import networkx as nx 
import pandas as pd 

class event:
    
    def __init__(self,label,source,target,unixtime):
        self.label=label
        self.source=source
        self.target=target
        self.unixtime=unixtime
    

        
    