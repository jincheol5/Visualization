import pandas as pd 
from pandas.plotting import parallel_coordinates
from event import Event
from data_set import data_set
import networkx as nx
import matplotlib.pyplot as plt
from visualization import draw_bipartite

data=data_set("data-10.txt")

parallel_coordinates(data.get_dataframe(),class_column="unix_time")

plt.show()