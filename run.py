import os

i = 8
while i < 130:
    u = 'C:/Users/reddy/Documents/2D-Maze-Solver/gen.py ' +str(i) + ' '+str(i)
    v = 'C:/Users/reddy/Documents/2D-Maze-Solver/main.py'
    os.system(u)
    os.system(v)
    print(i)
    i += 8