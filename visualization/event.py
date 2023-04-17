import networkx as nx 
import pandas as pd 

class event:
    
    def __init__(self,label,source,target,unixtime):
        self.label=label
        self.source=source
        self.target=target
        self.unixtime=unixtime
    
    def get_label(self):
        return self.label
    def get_source(self):
        return self.source
    def get_target(self):
        return self.target
    def get_unixtime(self):
        return self.unixtime
        
    