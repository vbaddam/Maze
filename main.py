import search
from graph import Graph
from time import time


if __name__ == "__main__":
    # Setting graph we initiated to search class...
    graph = Graph()
    search.graph = graph
    search.greedy_best_first_search()
    for _ in range(10):
        search.epsilon_greedy_best_first_search()
    
    search.iterative_deepening_search()