import pandas as pd
import math
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('epsilon-results.csv')

df = df.dropna()

ep = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8]
n = []
m = []
min_cost = []
expanded_nodes = []
j = 64
size = []
e = []
Algorithm = []
while j <= 104:
    n = []
    m = []
    
    
    for k in ep:
        e.append(k)
        size.append(j)
        for i in range(len(df['Algorithm'])):
            if df['Algorithm'].iloc[i] == 'eGFBS' and df['Size'].iloc[i] == j and df['epsilon'].iloc[i] == k:
                n.append(df['Solution Cost'].iloc[i])
                m.append(df['Expanded Nodes'].iloc[i])
        min_cost.append(min(n))
        expanded_nodes.append(math.floor(np.mean(m)))
        Algorithm.append('eGBFS')
        
    j = j + 8
                



d = pd.DataFrame(list(zip(size,Algorithm,
min_cost,
expanded_nodes,
e)), columns = ['Size',
'Algorithm',
'Cost', 
'Nodes', 
'epsilon'])

h = d['Cost'][:8]
k = d['Cost'][16:24]

y = np.linspace(0,8, 8)
fig, ax = plt.subplots(1)
ax.plot(y, h)
ax.plot(y, k)
ax.plot(y, d['Cost'][24:32])
ax.plot(y, d['Cost'][32:40])
ax.plot(y, d['Cost'][40:48])
ax.legend(['size 64', 'size 72', 'size 80', 'size 88', 'size 96', 'size 104'])
ax.set_ylabel('Optimal cost')
plt.savefig('plots/sensitivity.png')