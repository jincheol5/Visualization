
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
import pandas as pd



df = pd.read_csv('data/mydata-10.csv')

dataf=df.astype('string')


print(dataf)

parallel_coordinates(dataf,class_column='time')

plt.show()