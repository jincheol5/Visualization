import networkx as nx
import matplotlib.pyplot as plt



def draw_graph(nodes,events):
    graph=nx.Graph()
    g2=nx.Graph()
    
    graph.add_nodes_from(nodes)
    g2.add_nodes_from(nodes)    
    
    start_time=events[0].unix_time
    end_time=events[-1].unix_time

    for event in events:
        graph.add_edge(event.source,event.target)
        g2.add_edge(event.source,event.target)
    

    

    nx.draw(graph,node_color='blue', edge_color='blue')
    

    plt.show()



def draw_bipartite(nodes,events):
    graph = nx.Graph()
    
    start_time=events[0].unix_time
    end_time=events[-1].unix_time
    
    nodes_300000=[]
    nodes_600000=[]
    nodes_900000=[]
    
    
    
    
    for node in nodes:
        nodes_300000.append(node+"+300000")
        nodes_600000.append(node+"+600000")
        nodes_900000.append(node+"+600000")
        
    
    
    pos={}
    
    graph.add_nodes_from(nodes)
    graph.add_nodes_from(nodes_300000)
    graph.add_nodes_from(nodes_600000)
    graph.add_nodes_from(nodes_900000)
    
    for event in events:
        if int(event.unix_time)-int(start_time)<=300000:
            graph.add_edge(event.source,event.target+"+300000")
        elif int(event.unix_time)-int(start_time)<=600000:
            graph.add_edge(event.source+"+300000",event.target+"+600000")
        else:
            graph.add_edge(event.source+"+600000",event.target+"+900000")
    
    gap=1
    for node in nodes:
        pos[node]=[1,gap]
        gap+=10

    gap=1
    for node in nodes_300000:
        pos[node]=[10,gap]
        gap+=10 
        
    gap=1
    for node in nodes_600000:
        pos[node]=[15,gap]
        gap+=10 
        
    gap=1
    for node in nodes_900000:
        pos[node]=[20,gap]
        gap+=10 
    
    nx.draw(graph,pos,with_labels=True)
    
    plt.show()    

