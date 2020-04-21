import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

df = pd.read_csv('results.csv')

j = 8
size = []
GBFS = []
GBFS_nodes = []
GBFS_time = []
eGBFS_min = []
eGBFS_avg = []
eGBFS_nodes = []
eGBFS_time = []
IDS = []
IDS_nodes = []
IDS_time = []
while j < 64:
  a = []
  b = []
  c = []
  size.append(j)
  for i in range(0, len(df['Algorithm'])):
    
    if df['Algorithm'].iloc[i] == 'GBFS' and df['Size'].iloc[i] == j:
      GBFS.append(df['Solution Cost'].iloc[i])
      GBFS_nodes.append(df['Expanded Nodes'].iloc[i])
      GBFS_time.append(df['Time'].iloc[i])
    elif df['Algorithm'].iloc[i] == 'IDS' and df['Size'].iloc[i] == j:
      IDS.append(df['Solution Cost'].iloc[i])
      IDS_nodes.append(df['Expanded Nodes'].iloc[i])
      IDS_time.append(df['Time'].iloc[i])
    elif df['Algorithm'].iloc[i] == 'eGFBS' and df['Size'].iloc[i] == j:
      a.append(df['Solution Cost'].iloc[i])
      b.append(df['Expanded Nodes'].iloc[i])
      c.append(df['Time'].iloc[i])
  eGBFS_min.append(min(a))
  eGBFS_avg.append(np.mean(a))
  eGBFS_nodes.append(math.floor(np.mean(b)))
  eGBFS_time.append(np.mean(c))
  j = j + 8


d = pd.DataFrame(list(zip(size,GBFS,
GBFS_nodes,
GBFS_time,
eGBFS_min, 
eGBFS_avg, 
eGBFS_nodes,
eGBFS_time, 
IDS,
IDS_nodes,
IDS_time)), columns = ['size',
'GBFS',
'GBFS_nodes',
'GBFS_time', 
'eGBFS', 
'eGBFS_avg', 
'eGBFS_nodes',
'eGBFS_time', 
'IDS', 
'IDS_nodes',
'IDS_time'])


ax = d.plot(x = 'size', y = ['GBFS', 'eGBFS', 'IDS'], kind = 'bar')
ax.set_ylabel('Optimal Cost')
ax.set_title('Optimal Cost for three algorithms')
plt.savefig('plots/Optimal Cost(small size).png')


fig, (ax1,ax2) = plt.subplots(2)
ax1.plot(d['size'], d['GBFS_nodes'], label = 'GBFS')
ax1.plot(d['size'], d['eGBFS_nodes'], label = 'eGBFS')
ax1.set_ylabel('Time Complexity/Nodes Visited')
ax1.set_xlabel('Size')
legend = ax1.legend(loc=2, shadow=True)
legend.get_frame().set_facecolor('C7')
ax2.plot(d['size'], d['IDS_nodes'], label = 'IDS')
ax2.set_ylabel('Time Complexity/Nodes Visited')
ax2.set_xlabel('Size')
legend1 = ax2.legend(loc=2, shadow=True)
legend1.get_frame().set_facecolor('C7')
plt.savefig('plots/Time Complexity(small size)).png')


ax1 = d.plot(x = 'size', y = ['GBFS_time', 'eGBFS_time'], kind = 'bar')
ax1.set_ylabel('time(s)')
ax1.set_title('time elapses for GBFS and eGBFS')
plt.savefig('plots/Time Elapsed-small1.png')



ax2 = d.plot(x = 'size', y = ['IDS_time'], kind = 'bar')
ax2.set_ylabel('time(s)')
ax2.set_title('time elapses IDS')
plt.savefig('plots/Time Elapsed-small2.png')


j = 64
size = []
GBFS = []
GBFS_nodes = []
GBFS_time = []
eGBFS_min = []
eGBFS_avg = []
eGBFS_nodes = []
eGBFS_time = []
IDS = []
IDS_nodes = []
IDS_time = []
while j <= 104:
  a = []
  b = []
  c = []
  size.append(j)
  for i in range(0, len(df['Algorithm'])):
    
    if df['Algorithm'].iloc[i] == 'GBFS' and df['Size'].iloc[i] == j:
      GBFS.append(df['Solution Cost'].iloc[i])
      GBFS_nodes.append(df['Expanded Nodes'].iloc[i])
      GBFS_time.append(df['Time'].iloc[i])
    elif df['Algorithm'].iloc[i] == 'eGFBS' and df['Size'].iloc[i] == j:
      a.append(df['Solution Cost'].iloc[i])
      b.append(df['Expanded Nodes'].iloc[i])
      c.append(df['Time'].iloc[i])
  eGBFS_min.append(min(a))
  eGBFS_avg.append(np.mean(a))
  eGBFS_nodes.append(math.floor(np.mean(b)))
  eGBFS_time.append(np.mean(c))
  j = j + 8




d = pd.DataFrame(list(zip(size,GBFS,
GBFS_nodes,
GBFS_time,
eGBFS_min, 
eGBFS_avg, 
eGBFS_nodes,
eGBFS_time)), columns = ['size',
'GBFS',
'GBFS_nodes',
'GBFS_time', 
'eGBFS', 
'eGBFS_avg', 
'eGBFS_nodes',
'eGBFS_time'])


ax = d.plot(x = 'size', y = ['GBFS', 'eGBFS'], kind = 'bar')
ax.set_ylabel('Optimal Cost')
ax.set_title('Optimal Cost for two algorithms')
plt.savefig('plots/Optimal Cost(Large size).png')


fig, (ax1) = plt.subplots(1)
ax1.plot(d['size'], d['GBFS_nodes'], label = 'GBFS')
ax1.plot(d['size'], d['eGBFS_nodes'], label = 'eGBFS')
ax1.set_ylabel('Time Complexity/Nodes Visited')
ax1.set_xlabel('Size')
legend = ax1.legend(loc=2, shadow=True)
legend.get_frame().set_facecolor('C7')
plt.savefig('plots/Time Complexity(large).png')


ax1 = d.plot(x = 'size', y = ['GBFS_time', 'eGBFS_time'], kind = 'bar')
ax1.set_ylabel('time(s)')
ax1.set_title('time elapses for GBFS and eGBFS')
plt.savefig('plots/Time Elapsed(large).png')


