# Maze
A maze is a path or collection of paths, typically from an entrance to a goal. The main objective for any solver is to get to the terminal state/goal state from a given point. 
![img](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Longleat_maze.jpg/450px-Longleat_maze.jpg)

This program solves a maze with the help of several search algorithms like ***GBFS, IDS and eGBFS***. Generate file creates the maze with the desired dimension/size. The algorithms takes this generated file as input and solve the maze with the goal of obtaining a optimal path.

## Details

The generated file contains the information about maze. Each maze has the following attributes

- Maze Size; This gives the dimension of the maze. Contains in the format of rows and columns in a given matrix
- Wall Locations
- Trap Locations; Both the wall and trap locations are randomly generated and are randomly distributed throughout the maze. Solver will be penalised for getting into trap which would ultimately result in increase of cost.

- Goal Locations
- Start Location

![img](https://drive.google.com/open?id=1z9O8vYakwp9ymkWYD4LwtYUFTBFewRW0)

After generating and feeding the file into algorithms, they search for an optimal path. In this project, we mainly focused on these three algorithms. 

- Iterative-Deepening Search (IDS)
- Greedy-Best-First Search (GBFS)
- epsilon Greedy-Best-First Search (eGBFS).

I have develpoed epsilon Greedy-Best-First search inspiring from the epsilon based Reinforcement Learning. eGBFS outperforms the both IDS and GBFS in obtaining optimal cost.


