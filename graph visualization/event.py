

class Event:
    def __init__(self,source,target,unix_time):
        self.source=source
        self.target=target
        self.unix_time=unix_time
        
    def set_event(self,source,target,unix_time):
        self.source=source
        self.target=target
        self.unix_time=unix_time
        
    def toString(self):
        str="edge = "+self.source+" -> "+self.target+" at unixTime : "+self.unix_time
        return str