import numpy as np


class Node:
    def __init__(self, missionaries_wrong_side, cannibals_wrong_side, boat_wrong_side):
        self.state = (missionaries_wrong_side, cannibals_wrong_side, boat_wrong_side)
        self.missionaries_wrong_side = missionaries_wrong_side
        self.cannibals_wrong_side = cannibals_wrong_side
        self.boat_wrong_side = boat_wrong_side

    def is_goal_state(self):
        if self.missionaries_wrong_side == 0 and self.cannibals_wrong_side == 0:
            return True
        else:
            return False

    def is_valid_state(self):
        missionaries_left_side = self.missionaries_wrong_side
        missionaries_right_side = 3 - self.missionaries_wrong_side
        cannibals_left_side = self.cannibals_wrong_side
        cannibals_right_side = 3 - self.cannibals_wrong_side

        if missionaries_left_side >= 0 and missionaries_right_side >= 0 \
                and cannibals_left_side >= 0 and cannibals_right_side >= 0 \
                and (missionaries_left_side == 0 or missionaries_left_side >= cannibals_left_side) \
                and (missionaries_right_side == 0 or missionaries_right_side >= cannibals_right_side):
            return True
        else:
            return False

    def get_child_nodes(self):
        actions = [(1, 0, 1), (2, 0, 1), (0, 1, 1), (0, 2, 1), (1, 1, 1)]
        children = []
        for action in actions:
            if self.boat_wrong_side == 1:
                new_state = np.subtract(self.state, action)
            else:
                new_state = np.add(self.state, action)

            missionaries_wrong_side = new_state[0]
            cannibals_wrong_side = new_state[1]
            boat_wrong_side = new_state[2]
            child = Node(missionaries_wrong_side, cannibals_wrong_side, boat_wrong_side)

            if child.is_valid_state():
                children.append(child)
            else:
                continue

        return children

    def __eq__(self, other):
        return self.missionaries_wrong_side == other.missionaries_wrong_side \
               and self.cannibals_wrong_side == other.cannibals_wrong_side \
               and self.boat_wrong_side == other.boat_wrong_side

    # def __ne__(self, other):
    #    return not self == other

    def __hash__(self):
        return hash((self.missionaries_wrong_side, self.cannibals_wrong_side, self.boat_wrong_side))

