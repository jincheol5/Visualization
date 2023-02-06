import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3],
                'B': [4, 5, 6],
                'C': [7, 8, 9]})

fig, ax = plt.subplots()
ax.set_xticks([0, 1, 2])
ax.set_xticklabels(['A', 'B', 'C'])

for i in range(3):
    ax.plot(df.columns, df.iloc[i], '-o')

plt.xlim(-0.5, 2.5)
plt.ylim(0, 10)
plt.title('Parallel Coordinate Plot')
plt.show()