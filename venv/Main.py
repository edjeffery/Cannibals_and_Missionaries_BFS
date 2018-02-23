from Game import Game
from Node import Node

g = Game()
goal_node = g.breadth_first_search()
print("The goal node is", goal_node.state)