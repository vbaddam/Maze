import random
import sys
import math

arguments = sys.argv
r = arguments[1]
c = arguments[1]
f = open('maze3.txt', 'w')
f.write('Size\n')
f.write(r + ' rows\n')
f.write(c + ' columns\n')
f.write('\n')
f.close()




sequence = [i for i in range(int(r)-1)]
r = len(sequence)
f = open('maze3.txt', 'a')
f.write('Walls\n')
for i in range(1,r+1):
    f.write('row '+str(i)+'\n')
    o = random.randint(2,r-2)
    l = random.sample(sequence, o)
    for j in range(len(l)):
        f.write(str(l[j]))
        f.write(' ')
    f.write('\n')
f.close()


c = len(sequence)
f = open('maze3.txt', 'a')
for i in range(2,c):
    f.write('column '+str(i)+'\n')
    o = random.randint(2,r-2)
    l = random.sample(sequence, o)
    for j in range(len(l)):
        f.write(str(l[j]))
        f.write(' ')
    f.write('\n')
f.write('\n')
f.close()

s = [i for i in range(3,int(r)-2)]
t = [i for i in range(4,int(r)-2)]

f = open('maze3.txt', 'a')
f.write('Traps\n')
l = random.sample(s, math.floor(len(s)/2))
m = random.sample(t, math.floor(len(s)/2))
for i in range(len(l)):
    f.write(str(l[i])+' '+str(m[i]))
    f.write('\n')
f.write('\n')
f.close()


f = open('maze3.txt', 'a')
f.write('Start\n')
f.write('1 1\n')

f.write('\n')
f.write('Goals\n')

f.write(str(r) +' '+str(c))
f.close()
