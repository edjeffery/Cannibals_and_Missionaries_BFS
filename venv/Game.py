class Game:
    def __init__(self):
        self.initial_node = Node(missionaries_wrong_side=3, cannibals_wrong_side=3, boat_wrong_side=1)

    def breadth_first_search(self):
        if self.initial_node.is_goal_state():
            return self.initial_node
        frontier = []
        explored = set()
        frontier.append(self.initial_node)

        while frontier:
            node = frontier.pop(0)
            print("Exploring node " + str(node.state))
            explored.add(node)
            children = node.get_child_nodes()
            for child in children:
                if (child not in frontier) and (child not in explored):
                    if child.is_goal_state():
                        return child
                    frontier.append(child)

        return None
